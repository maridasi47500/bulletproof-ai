from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_phrasetraduire", methods=["GET","POST"])
def add_one_phrasetraduire():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into phrasetraduire (from_id,to_id,content) values (:from_id,:to_id,:content)",request.form)
        user = query_db('select * from phrasetraduire')
        return render_template("phrasetraduireform.html", phrasetraduires=user, one_user=one_user, the_title="add new phrasetraduire")
    user = query_db('select * from phrasetraduire')
    one_user = query_db("select * from phrasetraduire limit 1", one=True)
    return render_template("phrasetraduireform.html", phrasetraduires=user, one_user=one_user, the_title="add new phrasetraduire")

@app.route("/add_one_spokenlanguage", methods=["GET","POST"])
def add_one_spokenlanguage():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into spokenlanguage (name) values (:name)",request.form)
        user = query_db('select * from spokenlanguage')
        return render_template("spokenlanguageform.html", spokenlanguages=user, one_user=one_user, the_title="add new spokenlanguage")
    user = query_db('select * from spokenlanguage')
    one_user = query_db("select * from spokenlanguage limit 1", one=True)
    return render_template("spokenlanguageform.html", spokenlanguages=user, one_user=one_user, the_title="add new spokenlanguage")

@app.route("/add_one_programminglanguage", methods=["GET","POST"])
def add_one_programminglanguage():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into programminglanguage (name) values (:name)",request.form)
        user = query_db('select * from programminglanguage')
        return render_template("programminglanguageform.html", programminglanguages=user, one_user=one_user, the_title="add new programminglanguage")
    user = query_db('select * from programminglanguage')
    one_user = query_db("select * from programminglanguage limit 1", one=True)
    return render_template("programminglanguageform.html", programminglanguages=user, one_user=one_user, the_title="add new programminglanguage")

@app.route("/add_one_script", methods=["GET","POST"])
def add_one_script():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into script (content,programminglanguage_id,title) values (:content,:programminglanguage_id,:title)",request.form)
        user = query_db('select * from script')
        return render_template("scriptform.html", scripts=user, one_user=one_user, the_title="add new script")
    user = query_db('select * from script')
    one_user = query_db("select * from script limit 1", one=True)
    return render_template("scriptform.html", scripts=user, one_user=one_user, the_title="add new script")


__author__ = 'george'

from flask import Flask, render_template, request, make_response, json
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from database import init_db, db_session, drop_tables
import uuid
from models import Game, Cookie

app = Flask(__name__)

admin = Admin(app, name="superawesome game chooser")
admin.add_view((ModelView(Game, db_session)))
#games = ["Quake 1-2-3", "Unreal Tournament", "RA2"]

#Remove databses first, always start fresh
#drop_tables()
init_db()

g = None

#for game in games:
    #db_session.add(Game(game))run(
    #db_session.commit()




@app.route("/")
def index():
    user = request.cookies.get("uuid")
    games = []
    for row in Game.query.all():
        game = {}
        game["title"] = row.title
        game["num_likes"] = row.num_likes
        game["id"] = row.id
        games.append(game)
    print(games)
    if not user:
        newUser = str(uuid.uuid4().hex)
        #cookieDB.new_cookie(user)
    elif Cookie.query.filter(Cookie.uuid == user).first() == None:
        user = None
        newUser = str(uuid.uuid4().hex)

    if not user:

        resp = make_response(render_template("index.html", games=games))
        resp.set_cookie("uuid", newUser)
        print("returning with resp and uuid %s" % newUser)
        c = Cookie(newUser)
        db_session.add(c)
        db_session.commit()
        return resp
    else:
        u = Cookie.query.filter(Cookie.uuid == user).first()
        print(dir(Cookie.metadata.tables))
        print(u)
        try:
            likes_json = json.loads(u.likes)
        except TypeError:
            likes_json = json.loads(str([]))
        return render_template("index.html", games=games, likes=likes_json)


@app.route("/save", methods=["POST"])
def save_preferences():
    print("save")
    games = json.loads(request.get_data())
    uuid = request.cookies.get("uuid")
    print("uuid = %s" % uuid)
    user = Cookie.query.filter(Cookie.uuid == uuid).first()
    print(user)
    print(user.likes)
    user.likes = json.dumps(games)
    db_session.add(user)
    db_session.commit()
    return "200"

@app.route("/game/add", methods=["POST"])
def add_game():
    #data = json.loads(request.data())
    g = Game(title=request.form["title"])
    db_session.add(g)
    db_session.commit()
    return json.dumps({"id": g.id})

@app.route("/game/like/<int:id>")
def like(id):
    g = db_session.query(Game).filter_by(id=id).first()
    num_likes = g.num_likes
    num_likes += 1
    g.num_likes = num_likes
    db_session.add(g)
    db_session.commit()
    return "200"

@app.route("/game/unlike/<int:id>")
def unlike(id):
    g = db_session.query(Game).filter_by(id=id).first()
    num_likes = g.num_likes
    num_likes -= 1
    g.num_likes = num_likes
    db_session.add(g)
    db_session.commit()
    return "200"

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")



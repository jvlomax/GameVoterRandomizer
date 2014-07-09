__author__ = 'george'

from flask import Flask, render_template
import  sqlite3
app = Flask(__name__)

games = ["Quake 1-2-3", "Unreal Tournament"]


@app.route("/")
def index():
    return render_template("index.html", games=games)

if __name__ == "__main__":
    app.run(host="0.0.0.0")



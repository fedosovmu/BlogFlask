import sqlite3
import os
from flask import Flask, render_template, g
from blog_database import BlogDatabase

DATABASE = '/db/blog.db'
DEBUG = True
SECRET_KEY = 'c>{o_S3jcX3pMom^&vGDFyOf5I;erM-g7gHRL:-1caX4A5z@SxN<9~_iu@dKk*I'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update((dict(DATABASE=os.path.join(app.root_path, 'db/blog.db'))))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('db/sql/create_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/')
def index():
    db = get_db()
    dbase = BlogDatabase(db)
    return render_template('index.html', posts = dbase.get_posts())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)





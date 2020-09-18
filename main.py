import sqlite3
import os
from flask import Flask, render_template, g
from BlogDatabaseConnection import BlogDatabaseConnection

DATABASE = '/db/blog.db'
DEBUG = True
SECRET_KEY = 'c>{o_S3jcX3pMom^&vGDFyOf5I;erM-g7gHRL:-1caX4A5z@SxN<9~_iu@dKk*I'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update((dict(DATABASE=os.path.join(app.root_path, 'db/blog.db'))))


@app.route('/')
def index():
    db_connection = BlogDatabaseConnection(app, g)
    return render_template('index.html', posts = db_connection.get_posts())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db_connection'):
        g.db_connection.close()


if __name__ == '__main__':
    app.run(debug=True)





import sqlite3
import os
import locale
from flask import Flask, render_template, g, abort
from BlogDatabaseConnection import BlogDatabaseConnection


DATABASE_PATH = '/db/blog.db'
SECRET_KEY = 'c>{o_S3jcX3pMom^&vGDFyOf5I;erM-g7gHRL:-1caX4A5z@SxN<9~_iu@dKk*I'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update((dict(DATABASE_PATH=os.path.join(app.root_path, 'db/blog.db'))))

locale.setlocale(locale.LC_ALL, ('RU','UTF8'))

@app.route('/')
def index():
    blog_db_connection = BlogDatabaseConnection(app, g)
    return render_template('index.html', posts = blog_db_connection.get_posts())

@app.route('/post/<post_id>')
def post(post_id):
    blog_db_connection = BlogDatabaseConnection(app, g)
    post = blog_db_connection.get_post_by_id(post_id)
    if post:
        return render_template('post.html', post = post)
    else:
        abort(404)

@app.route('/debug/<command>')
def execute_command(command):
    if DEBUG:
        blog_db_connection = BlogDatabaseConnection(app, g)
        if command == 'execute_insert_test_data_script':
            blog_db_connection.execute_insert_test_data_script()
            return 'OK'
        elif command == 'execute_create_db_script':
            blog_db_connection.execute_create_db_script()
            return 'OK'
        elif command == 'execute_delete_all_posts_script':
            blog_db_connection.execute_delete_all_posts_script()
            return 'OK'
        elif command == 'test_info':
            return 'hello world'
        return 'unknown command'
    else:
        abort(404)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db_connection'):
        g.db_connection.close()

@app.errorhandler(404)
def pageNotFound(error):
    return '<h1>404 custom page</h1>', 404

if __name__ == '__main__':
    app.run(debug=True)





import sqlite3
import os
import locale
from flask import Flask, render_template, g, abort, request
from BlogDatabase import BlogDatabase


DATABASE_PATH = '/db/blog.db'
SECRET_KEY = 'c>{o_S3jcX3pMom^&vGDFyOf5I;erM-g7gHRL:-1caX4A5z@SxN<9~_iu@dKk*I'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update((dict(DATABASE_PATH=os.path.join(app.root_path, 'db/blog.db'))))

locale.setlocale(locale.LC_ALL, ('RU','UTF8'))
blog_db = BlogDatabase(app)

@app.route('/')
def index():
    blog_db.connect()
    return render_template('index.html', posts = blog_db.get_posts())

@app.route('/post/<post_id>')
def post(post_id):
    blog_db.connect()
    if request.method == 'POST':
        comment_text = request.data
        blog_db.add_comment_to_post_by_post_id(comment_text, post_id)

    post = blog_db.get_post_by_id(post_id)
    comments = blog_db.get_comments_by_post_id(post.post_id)
    if post:
        return render_template('post.html', post = post, comments = comments)
    else:
        abort(404)

@app.route('/script/<script_name>')
def execute_script(script_name):
    if app.debug:
        blog_db.connect()
        blog_db.execute_script(script_name)
    else:
        abort(404)

@app.teardown_appcontext
def close_db(error):
    blog_db.close_connection()

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)





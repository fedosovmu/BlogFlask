import sqlite3
from Post import Post
from Comment import Comment


class BlogDatabase:
    def __init__(self, app, g):
        if not hasattr(g, 'db_connection'):
            self.__app = app
            self.__g = g
            self.__db_connection = self.__connect_db(app)
            g.db_connection = self.__db_connection
            self.__cursor = self.__db_connection.cursor()
            self.__app = app

    def connect(self):
        if not hasattr(self.__g, 'db_connection'):
            db_connection = sqlite3.connect(self.__app.config['DATABASE_PATH'])
            db_connection.row_factory = sqlite3.Row
            self.__db_connection = db_connection
            self.__g.db_connection = self.__db_connection
            self.__cursor = self.__db_connection.cursor()

    def close_connection(self):
        if hasattr(self.__g, 'db_connection'):
            self.__g.close()

    def execute_script(self, script_name):
        with self.__app.open_resource('db/sql/' + script_name, mode='r') as script_file:
            self.__cursor.executescript(script_file.read())

    def get_posts(self):
        sql = 'SELECT post_id, title, short_description, text, publication_date, img_url FROM post'
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        posts = []
        for row in result:
            post = Post.create_from_db_row(row)
            posts.append(post)
        return posts

    def get_post_by_id(self, post_id):
        sql = 'SELECT post_id, title, short_description, text, publication_date, img_url FROM post WHERE post_id = ?'
        self.__cursor.execute(sql, (post_id,))
        row = self.__cursor.fetchone()
        if row:
            post = Post.create_from_db_row(row)
            return post
        return None

    def get_comments_by_post_id(self, post_id):
        sql = 'SELECT comment_id, post_id, text FROM comment WHERE post_id = ?'
        self.__cursor.execute(sql, (post_id,))
        result = self.__cursor.fetchall()
        comments = []
        for row in result:
            comment = Comment.create_from_db_row(row)
            comments.append(comment)
        return comments


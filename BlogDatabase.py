import sqlite3
from Post import Post
from Comment import Comment


class BlogDatabase:
    def __init__(self, app, g):
        self.__app = app
        self.__g = g

    def connect(self):
        if not hasattr(self.__g, 'db_connection'):
            db_connection = sqlite3.connect(self.__app.config['DATABASE_PATH'])
            db_connection.row_factory = sqlite3.Row
            self.__db_connection = db_connection
            self.__cursor = self.__db_connection.cursor()
            self.__g.db_connection = self.__db_connection

    def close_connection(self):
        if hasattr(self.__g, 'db_connection'):
            self.__g.db_connection.close()

    def execute_script(self, script_name):
        with self.__app.open_resource('db/sql/' + script_name, mode='r') as script_file:
            self.__cursor.executescript(script_file.read())

    def get_posts(self):
        sql = 'SELECT post_id, title, short_description, text, publication_date, img_url FROM post'
        self.__cursor.execute(sql)
        post_rows = self.__cursor.fetchall()
        posts = []
        for post_row in post_rows:
            post = Post(post_row['post_id'], post_row['title'], post_row['short_description'], post_row['text'], post_row['publication_date'], post_row['img_url'])
            posts.append(post)
        return posts

    def get_post_by_id(self, post_id):
        sql = 'SELECT post_id, title, short_description, text, publication_date, img_url FROM post WHERE post_id = ?'
        self.__cursor.execute(sql, (post_id,))
        post_row = self.__cursor.fetchone()
        if post_row:
            post = Post(post_row['post_id'], post_row['title'], post_row['short_description'], post_row['text'], post_row['publication_date'], post_row['img_url'])
            return post
        return None

    def get_comments_by_post_id(self, post_id):
        sql = 'SELECT comment_id, post_id, text FROM comment WHERE post_id = ?'
        self.__cursor.execute(sql, (post_id,))
        comment_rows = self.__cursor.fetchall()
        comments = []
        for comment_row in comment_rows:
            comment = Comment(comment_row['comment_id'], comment_row['post_id'], comment_row['text'])
            comments.append(comment)
        return comments


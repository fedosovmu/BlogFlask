import sqlite3
from Post import Post
from Comment import Comment


class BlogDatabase:
    def __init__(self, app):
        self.__app = app

    def connect(self):
        if not hasattr(self, '__db_connection'):
            db_connection = sqlite3.connect(self.__app.config['DATABASE_PATH'])
            db_connection.row_factory = sqlite3.Row
            self.__db_connection = db_connection
            self.__cursor = self.__db_connection.cursor()

    def close_connection(self):
        if hasattr(self, '__db_connection'):
            self.__db_connection.close()

    def execute_script(self, script_name):
        with self.__app.open_resource('db/sql/' + script_name, mode='r') as script_file:
            self.__cursor.executescript(script_file.read())

    @staticmethod
    def __create_post_from_db_row(row):
        return Post(row['post_id'], row['title'], row['short_description'], row['text'], row['publication_date'], row['img_url'])

    def get_posts(self):
        sql = 'SELECT post_id, title, short_description, text, publication_date, img_url FROM post'
        self.__cursor.execute(sql)
        post_rows = self.__cursor.fetchall()
        posts = []
        for post_row in post_rows:
            post = self.__create_post_from_db_row(post_row)
            posts.append(post)
        return posts

    def get_post_by_id(self, post_id):
        sql = 'SELECT post_id, title, short_description, text, publication_date, img_url FROM post WHERE post_id = ?'
        self.__cursor.execute(sql, (post_id,))
        post_row = self.__cursor.fetchone()
        if post_row:
            post = self.__create_post_from_db_row(post_row)
            return post
        return None

    @staticmethod
    def __create_comment_from_db_row(row):
        return Comment(row['comment_id'], row['post_id'], row['text'])

    def get_comments_by_post_id(self, post_id):
        sql = 'SELECT comment_id, post_id, text FROM comment WHERE post_id = ?'
        self.__cursor.execute(sql, (post_id,))
        comment_rows = self.__cursor.fetchall()
        comments = []
        for comment_row in comment_rows:
            comment = self.__create_comment_from_db_row(comment_row)
            comments.append(comment)
        return comments

    def add_comment_to_post_by_post_id(self, comment_text, post_id):
        sql = 'INSERT INTO comment (post_id, text) VALUES (?, ?)'
        self.__db_connection.commit()
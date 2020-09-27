import sqlite3
from Post import Post
from Comment import Comment


class BlogDatabaseConnection:
    def __init__(self, app, g):
        if not hasattr(g, 'db_connection'):
            self.__db_connection = self.__connect_db(app)
            g.db_connection = self.__db_connection
            self.__cursor = self.__db_connection.cursor()
            self.__app = app

    def __connect_db(self, app):
        db_connection = sqlite3.connect(app.config['DATABASE_PATH'])
        db_connection.row_factory = sqlite3.Row
        return db_connection

    def execute_create_db_script(self):
        with self.__app.open_resource('db/sql/create_db.sql', mode='r') as script_file:
            self.__cursor.executescript(script_file.read())

    def execute_insert_test_data_script(self):
        with self.__app.open_resource('db/sql/insert_test_data.sql', mode='r') as script_file:
            self.__cursor.executescript(script_file.read())

    def execute_delete_all_posts_script(self):
        sql_script = "DELETE FROM post"
        self.__cursor.executescript(sql_script)

    def get_posts(self):
        sql = 'SELECT post_id, title, short_description, publication_date, img_url FROM post'
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        posts = []
        for row in result:
            post = Post.create_from_db_row(row)
            posts.append(post)
        return posts

    def get_post_by_id(self, post_id):
        sql = 'SELECT post_id, title, short_description, publication_date, img_url FROM post WHERE post_id = ?'
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
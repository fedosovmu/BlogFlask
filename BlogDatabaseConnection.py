import sqlite3


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
        sql = '''SELECT post_id, title, short_description FROM post'''
        try:
            self.__cursor.execute(sql)
            res = self.__cursor.fetchall()
            if res: return res
        except:
            print('Ощибка чтения БД')
        return []
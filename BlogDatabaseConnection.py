import sqlite3

class BlogDatabaseConnection:
    def __init__(self, app, g):
        if not hasattr(g, 'db_connection'):
            g.db_connection = self.__connect_db(app)
        self.__db_connection = g.db_connection
        self.__cursor = self.__db_connection.cursor()


    def __connect_db(self, app):
        db_connection = sqlite3.connect(app.config['DATABASE'])
        db_connection.row_factory = sqlite3.Row
        return db_connection


    def execute_create_db_script(self, app):
        db_connection = self.__db_connection
        with app.open_resource('db/sql/create_db.sql', mode='r') as create_db_script:
            db_connection.cursor().executescript(create_db_script.read())
        db_connection.commit()
        db_connection.close()


    def get_posts(self):
        sql = '''SELECT * FROM post'''
        try:
            self.__cursor.execute(sql)
            res = self.__cursor.fetchall()
            if res: return res
        except:
            print('Ощибка чтения БД')
        return []
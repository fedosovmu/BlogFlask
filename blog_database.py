class BlogDatabase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_posts(self):
        sql = '''SELECT * FROM post'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('Ощибка чтения БД')
        return []
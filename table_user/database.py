import psycopg2
from utils.config import DataProject

class DataBase:
    db = None
    cursor = None
    secrets = DataProject()

    def connect(self) -> None:
        self.db = psycopg2.connect(
            dbname=self.secrets.DBNAME,
            user=self.secrets.USER_NAME,
            password=self.secrets.PASSWORD,
            host=self.secrets.HOST
        )
        self.cursor = self.db.cursor()

    def show_table(self):
        self.connect()
        self.cursor.execute('''
        SELECT * FROM admins
        ''')
        admins = self.cursor.fetchall()
        return admins

    def check_user(self, user_name):
        self.connect()
        self.cursor.execute(
            "SELECT * FROM admins WHERE name = md5(%s)", (user_name,)
        )
        user = self.cursor.fetchall()
        self.close_bd()
        return user

    def close_bd(self) -> None:
        self.cursor.close()
        self.db.close()



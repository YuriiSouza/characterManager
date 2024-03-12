
import psycopg2
import os
from dotenv import load_dotenv


class Database():
    def __init__(self):
        load_dotenv()

        self.HOST = os.getenv('HOST')
        self.USER = os.getenv('USER')
        self.PASSWORD = os.getenv('PASSWORD')


    def initDb(self):
        try:
            conn = psycopg2.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, )
            conn.cursor().execute('CREATE DATABASE teste')
            conn.close()
        except:
            print('database doesn`t work')


database = Database()

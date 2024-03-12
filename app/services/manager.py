from peewee import *
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

db = PostgresqlDatabase('managercharacters', host=HOST, user=USER, password=PASSWORD, port=5432)

class Characters(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField()
    description = CharField()
    link = CharField()
    show = CharField()
    animator = CharField()
    
    class Meta:
        database = db
        db_table='character'

db.connect()
db.create_tables([Characters])

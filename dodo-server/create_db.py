import uuid
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.auth import PlainTextAuthenticator
from models.lists_by_user import ListsByUser
from models.tasks_by_date import TasksByDate
from models.tasks_by_list_id import TasksByListId
from models.user import User
from passlib.hash import sha256_crypt


KEYSPACE = "dodo"

cluster = Cluster()
session = cluster.connect()
session.execute(
        """
        CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
        """ % KEYSPACE)
session = cluster.connect(keyspace=KEYSPACE)

connection.setup(['127.0.0.1'], "cqlengine", protocol_version=4)

def create_tables():
    sync_table(User)
    sync_table(ListsByUser)
    sync_table(TasksByListId)
    sync_table(TasksByDate)

def create_users():
    User.create(name="Milica", lastname="Petkovic", email="milica@elfak.rs", password=sha256_crypt.hash("123"))

def create_lists():
    list_id = uuid.uuid4()
    ListsByUser.create(list_id=list_id, user_email="milica@elfak.rs", list_name="shopping")

    TasksByDate.create(date="2022-12-25", user_email="milica@elfak.rs", task_id=uuid.uuid4(), task="Databases exam")
    TasksByDate.create(date="2022-12-25", user_email="milica@elfak.rs", task_id=uuid.uuid4(), task="Buy Christmas presents")

    TasksByListId.create(list_id=list_id, user_email="milica@elfak.rs", task_id=uuid.uuid4(), task="Milk", list_name="shopping")
    TasksByListId.create(list_id=list_id, user_email="milica@elfak.rs", task_id=uuid.uuid4(), task="Eggs", list_name="shopping")
    TasksByListId.create(list_id=list_id, user_email="milica@elfak.rs", task_id=uuid.uuid4(), task="Rice", list_name="shopping")
    TasksByListId.create(list_id=list_id, user_email="milica@elfak.rs", task_id=uuid.uuid4(), task="Soap", list_name="shopping")


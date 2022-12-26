from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes.auth import auth
from routes.task import task

from create_db import create_lists, create_tables, create_users

app = Flask(__name__)
CORS(app)
app.debug = True

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

if __name__ == "__main__":
    # create_tables()
    # create_users()
    # create_lists()
    app.register_blueprint(auth)
    app.register_blueprint(task)

    app.run()
    #connection.setup(['127.0.0.1'], "cqlengine", protocol_version=4)

    #sync_table(User)
    
    #session.execute("DROP TABLE lists_by_user")
    #sync_table(ListsByUser)
    # print("test")
    # list_id = uuid.uuid4()
    # list1 = ListsByUser.create(list_id = list_id, user_email='milica@elfak.rs', list_name='test2')

    #ListsByUser.create(user_email="test", list_name="test2")

    #objs = ListsByUser.objects
    #print("COUNT", objs.count())

    # res = session.execute("SELECT * FROM lists_by_user WHERE user_email = 'milica@elfak.rs'")
    # for r in res:
    #     print(r)


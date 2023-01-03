from datetime import datetime, date
from dateutil.parser import parse
import uuid
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, decode_token
from passlib.hash import sha256_crypt
from models.lists_by_user import ListsByUser
from models.tasks_by_date import TasksByDate

from models.tasks_by_list_id import TasksByListId

task = Blueprint("task", __name__)

@task.route("/task/create-list-task", methods=["POST"])
@jwt_required()
def create_list_task():
    req = request.get_json()

    list_id = req["listId"]
    task = str(req["task"])

    user_email = get_jwt_identity()

    # # for testing purposes
    # user_email = "milica@elfak.rs"

    # Check if fields are empty

    if not list_id:
        return {"listId": "This field is required."}, 400

    if not task:
        return {"task": "This field is required."}, 400
    
    list_obj = ListsByUser.objects(list_id=list_id, user_email=user_email).first()

    new_task = TasksByListId.create(list_id=list_id, user_email=user_email, task_id=uuid.uuid4(), task=task, \
                                    list_name=list_obj['list_name'])

    all_tasks = TasksByListId.objects(list_id=list_id, user_email=user_email)

    return jsonify({'tasks': [x.serialize() for x in all_tasks]}), 200

@task.route("/task/create-date-task", methods=["POST"])
def create_date_task():
    req = request.get_json()

    date = req["date"]
    task = str(req["task"])

    user_email = get_jwt_identity()

    # # for testing purposes
    # user_email = "milica@elfak.rs"

    # Check if fields are empty

    if not date:
        return {"date": "This field is required."}, 400

    if not task:
        return {"task": "This field is required."}, 400

    date = datetime.now()

    new_task = TasksByDate.create(date=date, user_email=user_email, task_id=uuid.uuid4(), task=task)

    return {'message':'OK'}, 200

@task.route("/task/check-task", methods=["PATCH"])
@jwt_required()
def check_task():
    req = request.get_json()

    task_id = req["taskId"]
    parent = req["parent"]

    user_email = get_jwt_identity()

    # # for testing purposes
    # user_email = "milica@elfak.rs"

    if not task_id:
        return {"task_id": "This field is required."}, 400

    if not parent:
        return {"parent": "This field is required."}, 400

    if is_date(parent):
        task = TasksByDate.objects(date=parent, user_email=user_email, task_id=task_id).first()
    else:
        task = TasksByListId.objects(list_id=parent, user_email=user_email, task_id=task_id).first()

    if not task:
        return jsonify({'error': 'There is no task object present in database'})

    task.completed = not task.completed
    if task.completed:
        task.completed_date = str(datetime.now())
    else:
        task.completed_date = None
    task.update()

    return jsonify({'task': task.serialize()}), 200

@task.route("/task/edit-task", methods=["PATCH"])
def edit_task():
    req = request.get_json()

    task_id = req["taskId"]
    parent = req["parent"]
    new_title = req["newTitle"]

    #user_email = get_jwt_identity() 

    # for testing purposes
    user_email = "milica@elfak.rs"

    if not task_id:
        return {"task_id": "This field is required."}, 400

    if not parent:
        return {"parent": "This field is required."}, 400
           
    if not new_title:
        return {"new_title": "This field is required."}, 400

    if is_date(parent):
        task = TasksByDate.objects(date=parent, user_email=user_email, task_id=task_id).first()
    else:
        task = TasksByListId.objects(list_id=parent, user_email=user_email, task_id=task_id).first()

    if not task:
        return jsonify({'error': 'There is no task object present in database'})

    task.task = new_title

    task.update()

    return jsonify({'task': dict(task)}), 200

@task.route("/task/delete-task", methods=["DELETE"])
def delete_task():
    req = request.get_json()

    task_id = req["taskId"]
    parent = req["parent"]

    #user_email = get_jwt_identity() 

    # for testing purposes
    user_email = "milica@elfak.rs"

    if not task_id:
        return {"task_id": "This field is required."}, 400

    if not parent:
        return {"parent": "This field is required."}, 400

    if is_date(parent):
        task = TasksByDate.objects(date=parent, user_email=user_email, task_id=task_id).first()
    else:
        task = TasksByListId.objects(list_id=parent, user_email=user_email, task_id=task_id).first()

    if not task:
        return jsonify({'error': 'There is no task object present in database'})

    task.delete()

    return jsonify({'message': "Task is successfully deleted"}), 200

@task.route("/task/get-tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    parent = request.args.get('parent')

    user_email = get_jwt_identity() 

    # for testing purposes
    #user_email = "milica@elfak.rs"

    if not parent:
        return {"parent": "This field is required."}, 400

    if is_date(parent):
        print("dateeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        tasks = TasksByDate.objects(date=parent, user_email=user_email)
    else:
        print("listaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        tasks = TasksByListId.objects(list_id=parent, user_email=user_email)

    return jsonify({'tasks': [x.serialize() for x in tasks]}), 200

@task.route("/task/get-lists", methods=["GET"])
@jwt_required()
def get_lists():
    user_email = get_jwt_identity() 

    # for testing purposes
    #user_email = "milica@elfak.rs"

    lists = ListsByUser.objects(user_email=user_email)

    return jsonify({'lists': [x.serialize() for x in lists]}), 200

@task.route("/task/create-list", methods=["POST"])
@jwt_required()
def create_list():
    req = request.get_json()

    list_name = req["listName"]

    user_email = get_jwt_identity()

    # # for testing purposes
    # user_email = "milica@elfak.rs"

    if not list_name:
        return {"listName": "This field is required."}, 400

    new_list = ListsByUser.create(list_name=list_name, user_email=user_email, list_id=uuid.uuid4())

    return jsonify({'list': new_list.serialize()}), 200


def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False
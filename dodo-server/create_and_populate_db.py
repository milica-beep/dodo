import uuid
from models.lists_by_user import ListsByUser
from models.tasks_by_date import TasksByDate
from models.tasks_by_list_id import TasksByListId
from models.user import User
from passlib.hash import sha256_crypt
import db_con
from cassandra.cqlengine.management import sync_table

sync_table(User)
sync_table(ListsByUser)
sync_table(TasksByListId)
sync_table(TasksByDate)

User.create(name="Milica", lastname="Petkovic", email="milica@elfak.rs", password=sha256_crypt.hash("123"))
User.create(name="Test", lastname="TestTest", email="test@elfak.rs", password=sha256_crypt.hash("123"))

list_id = uuid.uuid4()
ListsByUser.create(list_id=list_id, user_email="milica@elfak.rs", list_name="shopping")

TasksByDate.create(date="2022-12-25", user_email="milica@elfak.rs", task_id=uuid.uuid4(), task="Databases exam")
TasksByDate.create(date="2022-12-25", user_email="milica@elfak.rs", task_id=uuid.uuid4(), task="Buy Christmas presents")

TasksByListId.create(list_id=list_id, user_email="milica@elfak.rs", task_id=uuid.uuid4(), task="Milk")
TasksByListId.create(list_id=list_id, user_email="milica@elfak.rs", task_id=uuid.uuid4(), task="Eggs")
TasksByListId.create(list_id=list_id, user_email="milica@elfak.rs", task_id=uuid.uuid4(), task="Rice")
TasksByListId.create(list_id=list_id, user_email="milica@elfak.rs", task_id=uuid.uuid4(), task="Soap")
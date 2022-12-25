import datetime
import uuid
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns

class TasksByListId(Model):
    __keyspace__ = 'dodo'
    list_id = columns.UUID(primary_key=True)
    user_id = columns.UUID(primary_key=True)
    task_id = columns.UUID(primary_key=True)
    task = columns.Text()
    completed = columns.Boolean(default=False)
    completed_date = columns.Date()
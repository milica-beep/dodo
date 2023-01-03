import datetime
import uuid
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns

class TasksByDate(Model):
    __keyspace__ = 'dodo'
    date = columns.Text(primary_key=True)
    user_email = columns.Text(primary_key=True)
    task_id = columns.UUID(primary_key=True)
    task = columns.Text()
    completed = columns.Boolean(default=False)
    completed_date = columns.Text()

    def serialize(self):
        return {'date': self.date, 'userEmail': self.user_email, 'taskId': self.task_id, \
                'task': self.task, 'completed': self.completed, 'completed_date': self.completed_date } 
                 
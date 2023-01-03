import uuid
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns

class ListsByUser(Model):
    __keyspace__ = 'dodo'
    user_email = columns.Text(primary_key=True)
    list_id = columns.UUID(primary_key=True)
    list_name = columns.Text()

    def serialize(self):
        return {'userEmail': self.user_email, 'listId': self.list_id, 'listName': self.list_name }
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns

class User(Model):
    __keyspace__ = 'dodo'
    email = columns.Text(primary_key=True)
    name = columns.Text()
    lastname = columns.Text()
    password = columns.Text()
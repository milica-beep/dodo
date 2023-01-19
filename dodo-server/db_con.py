from cassandra.cluster import Cluster
from cassandra.cqlengine import connection

KEYSPACE = "dodo"
cluster = Cluster()
session = cluster.connect()
session.execute(
        """
        CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
        """ % KEYSPACE)
session = cluster.connect(keyspace=KEYSPACE)

connection.setup(['127.0.0.1'], "cqlengine", protocol_version=4)
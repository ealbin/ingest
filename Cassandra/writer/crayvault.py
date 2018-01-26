"""CRAYFIS Cassandra Database
"""

from cassandra.cluster import Cluster

__cluster_nodes = [ 'crayvault' ]
__cluster = Cluster( __cluster_nodes )

def get_session():
    return __cluster.connect()

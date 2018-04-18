"""CRAYFIS Cassandra Database
"""

# get server IP address
import docker
__client = docker.from_env()
__server = __client.containers.get('crayvault')
__ipaddr = __server.attrs['NetworkSettings']['IPAddress']

# connect to the server
from cassandra.cluster import Cluster

__cluster = Cluster([__ipaddr])

def get_session():
    return __cluster.connect()

"""Access interface to Cassandra
"""

import writer

def insert( table='', names='', values='' ):
    writer.insert( table=table, names=names, values=values )

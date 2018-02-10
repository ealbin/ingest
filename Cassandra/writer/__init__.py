"""Access interface to Cassandra
"""

import writer

def insert( table='', names='', values='' ):
    return writer.insert( table=table, names=names, values=values )

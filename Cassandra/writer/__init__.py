"""Access interface to Cassandra
"""

import crayvault
import init_raw
import format

__session = None
try:
    __session = crayvault.get_session()
except Exception as e:
    print 
    print 'ERROR: failed to connect with crayvault'

import pdb
def insert( table='', names='', values='' ):
    print 'Writing: {0}'.format(table)
    print '\t{0}...{1}  <=>  {2}...{3}'.format(names[:20], names[-20:], values[:20], values[-20:])
    command  = """INSERT INTO {0} ( {1} ) VALUES ( {2} ) IF NOT EXISTS;""".format( table, names, values )
    try:
        __session.execute( command )
    except Exception as e:
        pdb.set_trace()
        print
        print 'ERROR: fail to insert,'
        print '     INSERT into ' + table + ' ( ' + names + ' )'
        print '     VALUES ( ' + values + ' ) '
        print





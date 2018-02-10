"""Access interface to Cassandra
"""

import crayvault
import init_raw
import compose

import time

__session = None

try:
    __session = crayvault.get_session()
except Exception as e:
    print 
    print 'ERROR: failed to connect with crayvault'

def insert( table='', names='', values='' ):
    starttime = time.time()
#    print 'Writing: {0}'.format(table)
#    print '\t{0}...{1}  <=>  {2}...{3}'.format(names[:20], names[-20:], values[:20], values[-20:])
    command  = """INSERT INTO {0} ( {1} ) VALUES ( {2} ) IF NOT EXISTS;""".format( table, names, values )
    try:
        __session.execute( command )
#        print '\tinsertion time: {0:.3} ms'.format( (time.time() - starttime) * 1000. )
    except Exception as e:
        print
        print 'ERROR: {0}'.format(e)
        print '     INSERT into ' + table + ' ( ' + names + ' )'
        print '     VALUES ( ' + values + ' ) '
        print





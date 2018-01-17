"""Cassandra interface

inteded use:
------------

    get_football()
        The football is a python object for mapping the names
        of Cassandra table columns across multiple tables in
        multiple keyspaces to their respective values.  It
        gets passed down the CrayonMessage hierarchy, and
        writes to Cassandra as data is ingested.
"""
__debug_mode = True

import raw_keyspace

class __BallBag:
    """private class to isolate the user
    from multiple keyspace footballs.
    If there are multiple keyspaces..
    """
    def __init__(self):
        """create new ballbag with footballs
        from each keyspace
        """
        self.clear()
        
    def clear(self):
        """clear all footballs of data
        """
        raw_keyspace.clear()

    def add_error(self, error):
        """log an error message
        """
        raw_keyspace.add_error( error )
            
    def get_n_errors(self):
        """return N errors logged
        """
        return raw_keyspace.get_n_errors()

    def set_metadata(self, host='', tarfile='', tarmember=''):
        """log metadata
        """
        host = repr(host)
        raw_keyspace.set_metadata( host=host, tarfile=tarfile, tarmember=tarmember )

    def set_serialized(self, serialized_string ):
        """log raw, serialized CrayonMessage
        """
        raw_keyspace.set_serialized( serialized_string )
    
    def set_headers(self, basics):
        """log CrayonMessage headers
        """
        raw_keyspace.set_headers( basics )


    def insert_misfit(self):
        """INSERT misfit object into Cassandra
        """
        return raw_keyspace.insert_misfit()

    def insert_runconfig(self, basics):
        """INSERT runconfig object into Cassandra
        """ 
        return raw_keyspace.insert_runconfig( basics )
        
    def insert_calibration_result(self, basics):
        """INSERT calibration_result object into Cassandra
        """
        return raw_keyspace.insert_calibration_result( basics )

    def insert_precalibration_result(self, basics):
        """INSERT precalibration_result object into Cassandra
        """
        return raw_keyspace.insert_precalibration_result( basics )

    def insert_exposure_block(self, basics, daq_state='', event_ids=[]):
        """INSERT exposure_block object into Cassandra
        """
        return raw_keyspace.insert_exposure_block( basics, daq_state=daq_state, event_ids=event_ids )

    def insert_event(self, basics):
        """INSERT event object into Cassandra
        """
        return raw_keyspace.insert_event( basics )

# TODO:
#    def add_pixel( pixel ):
#    def add_zbias( zerobias ):
#    def add_byteb( byteblock ):
    
__football = __BallBag()
if __debug_mode: print '[Cassandra] football is ready'

def get_football():
    """Returns football.
    The football is a python object for mapping the names
    of Cassandra table columns across multiple tables in
    multiple keyspaces to their respective values.
    """
    if __debug_mode: print '[Cassandra] passing football'
    return __football

#def write_football():
#    """write football to Cassandra
#    """
#    global __football
#    if not len(__football['error_string']) == 0:
#        print __football['error_string']
#    else:
#        for [k, v] in __football.viewitems():
#            print '{0}_____: {1}'.format( k.upper(), repr(v)[:1000] )
#        print '\n\n'    
#        print __football['crayon_message']
#        print __football['exposure_blocks']
#        print __football['run_configs']
#        print __football['calibration_results']
#        print __football['precalibration_results']
#    for [f,v] in __football.viewitems():
#        print f, v


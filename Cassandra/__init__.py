"""Cassandra interface

inteded use:
------------

    get_football()
        The football interfaces the back-end of 
        how and what to write to Cassandra across 
        tables across keyspaces.  Pass it around,
        and ask it to write for you.
        
        intended use:
            football = get_football()
            football.clear() # to reset at any time
            e.g.
                football.insert_run_config( basics ) 
"""
__debug_mode = False

import raw_keyspace

class __BallBag:
    """private class to isolate the user
    from multiple keyspace footballs...
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
    
    # Errors and shared data
    #-----------------------
    def add_error(self, error):
        """log an error message
        """
        raw_keyspace.add_error( error )

    def get_n_errors(self):
        """return N errors logged
        """
        return raw_keyspace.get_n_errors()

    def get_event_uuid(self):
        """return current event uuid
        """
        return raw_keyspace.get_event_uuid()

    def set_metadata(self, host='', tarfile='', tarmember=''):
        """log metadata
        """
        host = repr(host)
        is_sucessful = raw_keyspace.set_metadata( host=host, tarfile=tarfile, tarmember=tarmember )
        return is_sucessful

    def set_serialized(self, serialized_string ):
        """log raw, serialized CrayonMessage
        """
        is_sucessful = raw_keyspace.set_serialized( serialized_string )
        return is_sucessful
    
    def set_headers(self, basics):
        """log CrayonMessage headers
        """
        is_sucessful = raw_keyspace.set_headers( basics )
        return is_sucessful

    # Specific insertions
    #--------------------
    def insert_misfit(self):
        """INSERT misfit object into Cassandra
        """
        is_sucessful = raw_keyspace.insert_misfit()
        return is_sucessful

    def insert_run_config(self, basics):
        """INSERT runconfig object into Cassandra
           Parameters:
               basics : Google protobuf field descriptor object and value
        """ 
        is_sucessful = raw_keyspace.insert_run_config( basics )
        return is_sucessful
        
    def insert_calibration_result(self, basics):
        """INSERT calibration_result object into Cassandra
           Parameters:
               basics : Google protobuf field descriptor object and value        
        """
        is_sucessful = raw_keyspace.insert_calibration_result( basics )
        return is_sucessful

    def insert_precalibration_result(self, basics, compressed_weights=''):
        """INSERT precalibration_result object into Cassandra
           Parameters:
               basics : Google protobuf field descriptor object and value
               
               compressed_weights : string
                                    Serialized weights        
        """
        is_sucessful = raw_keyspace.insert_precalibration_result( basics, compressed_weights=compressed_weights )
        return is_sucessful

    def insert_exposure_block(self, basics, daq_state='', event_ids=[]):
        """INSERT exposure_block object into Cassandra
           Parameters:
               basics    : Google protobuf field descriptor object and value
                           Collection of basic data types (no objects).
                           
               daq_state : string
                           Decoded daq_state enum string.
                           
               event_ids : array
                           UUIDs of related events that occured in this block.
        """
        is_sucessful = raw_keyspace.insert_exposure_block( basics, daq_state=daq_state, event_ids=event_ids )
        return is_sucessful

    def insert_event(self, basics, pixels=[], byteblock={}, zerobias={}):
        """INSERT event object into Cassandra
           Parameters:
               basics    : Google protobuf field descriptor object and value 
               
               pixels    : array of name-value attribute pairs for pixels
               
               byteblock : name-value attribute pairs for byteblock
               
               zerobias  : name-value attribute pairs for zero bias square
        """
        is_sucessful = raw_keyspace.insert_event( basics, pixels=pixels, byteblock=byteblock, zerobias=zerobias )
        return is_sucessful

#-----------------------------------------------------------------------------

__football = __BallBag()
if __debug_mode: print '[Cassandra] football is ready'

def get_football():
    """Returns football.
    The football interfaces the back-end of 
    how and what to write to Cassandra across 
    tables across keyspaces.  Pass it around,
    and ask it to write for you.
    
    intended use:
        football = get_football()
        football.clear() # to reset at any time
        e.g.
            football.insert_run_config( basics ) 
    """
    if __debug_mode: print '[Cassandra] passing football'
    return __football

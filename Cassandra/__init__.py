"""Cassandra interface

inteded use:
------------

    get_football()
        The football interfaces the back-end of 
        how and what to write to Cassandra across 
        tables across keyspaces.  Pass it around,
        and ask it to write for you.
        *note, once written to Cassandra, data is 
        purged from the football automatically.
        
        intended use:
            football = get_football()
            football.clear() # to reset at any time
            e.g.
                football.insert_run_config( basics ) 
                (run_config object is written to Cassandra,
                then cleared automatically)
"""
__debug_mode = False

import raw_keyspace
import writer

########################
# initialize Cassandra #
########################
writer.init_raw.clear()  # comment out to save database
writer.init_raw.do_it()  # tells Cassandra the structure

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

    def insert_exposure_block(self, basics, daq_state='', block_uuid=None, n_events=0):
        """INSERT exposure_block object into Cassandra
           Parameters:
               basics     : Google protobuf field descriptor object and value
                            Collection of basic data types (no objects).
                           
               daq_state  : string
                            Decoded daq_state enum string.
                           
               block_uuid : uuid.uuid5( uuid.NAMESPACE_DNS, string )
                            SHA1 hash UUID composed of a string: start_time+end_time to identify this block.
                            
               n_events   : int
                            Number of events in this exposure block
        """
        is_sucessful = raw_keyspace.insert_exposure_block( basics, daq_state=daq_state, block_uuid=block_uuid, n_events=n_events )
        return is_sucessful

    def insert_event(self, basics, block_basics=None, daq_state='', block_uuid=None, pixels=[], byteblock={}, zerobias={}):
        """INSERT event object into Cassandra
           Parameters:
               basics       : Google protobuf field descriptor object and value 
               
               block_basics : Google protobuf field descriptor object and value
                              from cooresponding exposure block for denormalization
               
               daq_state    : string, decoded daq_state enum string              

               block_uuid   : unique identifier to parent exposure block
               
               pixels       : array of name-value attribute pairs for pixels
               
               byteblock    : name-value attribute pairs for byteblock
               
               zerobias     : name-value attribute pairs for zero bias square
        """
        is_sucessful = raw_keyspace.insert_event( basics, block_basics=block_basics, daq_state=daq_state, block_uuid=block_uuid, pixels=pixels, byteblock=byteblock, zerobias=zerobias )
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

"""Cassandra keyspace: `raw`

intended use:
-------------
    Internals of the Cassandra football.
    Handles neuances unique to the `raw` keyspace.
    
    Tables:
        misfits
        exposure_blocks
        events
        runconfigs
        calibration_results
        precalibration_results
"""    

import raw_keyspace

def clear():
    raw_keyspace.clear()

# Errors and shared data
#-----------------------
def add_error( error_string ):
    raw_keyspace.add_error( error_string )
    
def get_n_errors():
    return raw_keyspace.get_n_errors()

def set_metadata(host='', tarfile='', tarmember=''):
    return raw_keyspace.set_metadata(host=host, tarfile=tarfile, tarmember=tarmember)

def set_serialized( serialized_string ):
    return raw_keyspace.set_serialized( serialized_string )
    
def set_headers( basics ):
    return raw_keyspace.set_headers( basics )

# Specific insertions
#--------------------
def insert_misfit():
    return raw_keyspace.insert_misfit()
    
def insert_run_config( basics ):
    return raw_keyspace.insert_run_config( basics )

def insert_calibration_result( basics ):
    return raw_keyspace.insert_calibration_result( basics )

def insert_precalibration_result( basics, compressed_weights='' ):
    return raw_keyspace.insert_precalibration_result( basics, compressed_weights=compressed_weights )

def insert_exposure_block( basics, daq_state='', block_uuid=None, n_events=0 ):
    return raw_keyspace.insert_exposure_block( basics, daq_state=daq_state, block_uuid=block_uuid, n_events=n_events )
    
def insert_event( basics, block_basics=None, daq_state='', block_uuid=None, pixels=[], byteblock={}, zerobias={} ):
    return raw_keyspace.insert_event( basics, block_basics=block_basics, daq_state=daq_state, block_uuid=block_uuid, pixels=pixels, byteblock=byteblock, zerobias=zerobias )

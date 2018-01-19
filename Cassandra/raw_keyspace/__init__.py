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
__debug_mode = False

import Misfit
import ExposureBlock
import Event
import RunConfig
import CalibrationResult
import PreCalibrationResult

import write

misfit                = Misfit.Football()
exposure_block        = ExposureBlock.Football()
event                 = Event.Football()
run_config            = RunConfig.Football()
calibration_result    = CalibrationResult.Football()
precalibration_result = PreCalibrationResult.Football()
n_errors = 0

def clear():
    global n_errors
    n_errors = 0
    misfit               .clear()
    exposure_block       .clear()
    event                .clear()
    run_config           .clear()
    calibration_result   .clear()
    precalibration_result.clear()
    if __debug_mode: print '[raw_keyspace] football cleared'

# Errors and shared data
#-----------------------
def add_error( error_string ):
    global n_errors
    n_errors += 1
    misfit.add_error( error_string )
    if __debug_mode: print '[raw_keyspace] error added'
    
def get_n_errors():
    return n_errors

def set_metadata(host='', tarfile='', tarmember=''):
    is_sucessful  = misfit               .set_metadata( host=host, tarfile=tarfile, tarmember=tarmember )
    is_sucessful &= exposure_block       .set_metadata( host=host, tarfile=tarfile, tarmember=tarmember )
    is_sucessful &= event                .set_metadata( host=host, tarfile=tarfile, tarmember=tarmember )
    is_sucessful &= run_config           .set_metadata( host=host, tarfile=tarfile, tarmember=tarmember )
    is_sucessful &= calibration_result   .set_metadata( host=host, tarfile=tarfile, tarmember=tarmember )
    is_sucessful &= precalibration_result.set_metadata( host=host, tarfile=tarfile, tarmember=tarmember )
    if __debug_mode: print '[raw_keyspace] metadata set: ' + host[:20] + '...' + tarfile[-20:] + ' ' + tarmember
    return is_sucessful

def set_serialized( serialized_string ):
    is_sucessful = misfit.set_serialized( serialized_string )
    if __debug_mode: print '[raw_keyspace] serialized message set'
    return is_sucessful
    
def set_headers( basics ):
    is_sucessful  = misfit               .set_basics( basics )
    is_sucessful &= exposure_block       .set_basics( basics )
    is_sucessful &= event                .set_basics( basics )
    is_sucessful &= run_config           .set_basics( basics )
    is_sucessful &= calibration_result   .set_basics( basics )
    is_sucessful &= precalibration_result.set_basics( basics )
    if __debug_mode: print '[raw_keyspace] headers set'
    return is_sucessful

# Specific insertions
#--------------------
def insert_misfit():
    write.insert( names=misfit.get_names(), values=misfit.get_values() )
    return True
    
def insert_run_config( basics ):
    run_config.set_basics( basics )
    write.insert( names=run_config.get_names(), values=run_config.get_values() )
    return True

def insert_calibration_result( basics ):
    calibration_result.set_basics( basics )
    write.insert( names=calibration_result.get_names(), values=calibration_result.get_values() )
    return True

def insert_precalibration_result( basics ):
    precalibration_result.set_basics( basics )
    write.insert( names=precalibration_result.get_names(), values=precalibration_result.get_values() )
    return True

def insert_exposure_block( basics, daq_state='', event_ids=[] ):
    exposure_block.set_basics( basics, daq_state=daq_state, event_ids=event_ids )
    write.insert( names=exposure_block.get_names(), values=exposure_block.get_values() )
    return True
    
def insert_event( basics ):
    event.set_basics( basics )    
    write.insert( names=eventsget_names(), values=event.get_values() )
    return True

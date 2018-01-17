"""Cassandra keyspace: `raw`

intended use:
-------------
    Intended to be called by Cassandra interface.
    Handles neuances unique to the `raw` keyspace.
    
    Tables:
        misfits
        exposure_blocks
        events
        runconfigs
        calibration_results
        precalibration_results
"""    

import Misfit
import ExposureBlock
import Event
import RunConfig
import CalibrationResult
import PreCalibrationResult

misfit                = Misfit.Football()
exposure_block        = ExposureBlock.Football()
event                 = Event.Football()
run_config            = RunConfig.Football()
calibration_result    = CalibrationResult.Football()
precalibration_result = PreCalibrationResult.Football()
n_errors = 0

def clear():
    misfit               .clear()
    exposure_block       .clear()
    event                .clear()
    run_config           .clear()
    calibration_result   .clear()
    precalibration_result.clear()
    n_errors = 0

def add_error( error_string ):
    misfit.add_error( error_string )
    n_errors += 1
    
def get_n_errors():
    return n_errors

def set_metadata(host='', tarfile='', tarmember=''):
    misfit               .set_metadata( host=host, tarfile=tarfile, tarmember=tarmember )
    exposure_block       .set_metadata( host=host, tarfile=tarfile, tarmember=tarmember )
    event                .set_metadata( host=host, tarfile=tarfile, tarmember=tarmember )
    run_config           .set_metadata( host=host, tarfile=tarfile, tarmember=tarmember )
    calibration_result   .set_metadata( host=host, tarfile=tarfile, tarmember=tarmember )
    precalibration_result.set_metadata( host=host, tarfile=tarfile, tarmember=tarmember )

def set_serialized( serialized_string ):
    misfit.set_serialized( serialized_string )
    
def set_headers( basics ):
    is_sucessful  = True
    is_sucessful &= misfit               .set_basics( basics )
    is_sucessful &= exposure_block       .set_basics( basics )
    is_sucessful &= event                .set_basics( basics )
    is_sucessful &= run_config           .set_basics( basics )
    is_sucessful &= calibration_result   .set_basics( basics )
    is_sucessful &= precalibration_result.add_basics( basics )
#    return is_sucessful
    
def insert_run_config( basics ):
    if run_config.set_basics( basics ):
        run_config.write
#    return run_config.set_basics( basics )
    run_config.set_basics( basics )

def insert_calibration_result( basics ):
    return calibration_result.set_basics( basics )

def insert_precalibration_result( basics ):
    return precalibration_result.set_basics( basics )

def insert_exposure_block( basics, daq_state='', event_ids=[] ):
    exposure_block.daq_state = daq_state
    exposure_block.event_ids = event_ids
    return exposure_block.set_basics( basics )
    
def insert_event( basics ):
    return event.set_basics( basics )

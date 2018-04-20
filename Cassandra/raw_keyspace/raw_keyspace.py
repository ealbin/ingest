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

from .. import writer

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
    is_sucessful  = misfit               .set_attributes( basics )
    is_sucessful &= exposure_block       .set_attributes( basics )
    is_sucessful &= event                .set_attributes( basics )
    is_sucessful &= run_config           .set_attributes( basics )
    is_sucessful &= calibration_result   .set_attributes( basics )
    is_sucessful &= precalibration_result.set_attributes( basics )
    if __debug_mode: print '[raw_keyspace] headers set'
    return is_sucessful

# Specific insertions
#--------------------
def insert_misfit():
    is_sucessful = writer.insert( table='raw.misfits', names=misfit.get_names(), values=misfit.get_values() )
    if not is_sucessful:
        print '[WARNING] FAILURE TO LOG MISFIT'
        print '          errors: {0}'.format(misfit.errors)
        print '          file: {0}'.format(misfit.tarfile)
        print '          member: {0}'.format(misfit.tarmember)
    clear()
    return is_sucessful
    
def insert_run_config( basics ):
    run_config.set_attributes( basics )
    is_sucessful = writer.insert( table='raw.run_configs', names=run_config.get_names(), values=run_config.get_values() )
    if not is_sucessful:
        print '[ISSUE] run config'
        print '      errors: {0}'.format(misfit.errors)
        print '      file: {0}'.format(misfit.tarfile)
        print '      member: {0}'.format(misfit.tarmember)
    run_config.reset()
    return is_sucessful

def insert_calibration_result( basics ):
    calibration_result.set_attributes( basics )
    is_sucessful = writer.insert( table='raw.calibration_results', names=calibration_result.get_names(), values=calibration_result.get_values() )
    if not is_sucessful:
        print '[ISSUE] calibration result'
        print '      errors: {0}'.format(misfit.errors)
        print '      file: {0}'.format(misfit.tarfile)
        print '      member: {0}'.format(misfit.tarmember)
    calibration_result.reset()
    return is_sucessful

def insert_precalibration_result( basics, compressed_weights='' ):
    precalibration_result.set_attributes( basics, compressed_weights=compressed_weights )
    is_sucessful = writer.insert( table='raw.precalibration_results', names=precalibration_result.get_names(), values=precalibration_result.get_values() )
    if not is_sucessful:
        print '[ISSUE] precalibration result'
        print '      errors: {0}'.format(misfit.errors)
        print '      file: {0}'.format(misfit.tarfile)
        print '      member: {0}'.format(misfit.tarmember)
    precalibration_result.reset()
    return is_sucessful

def insert_exposure_block( basics, daq_state='', block_uuid=None, n_events=0 ):
    exposure_block.set_attributes( basics, daq_state=daq_state, block_uuid=block_uuid, n_events=n_events )
    is_sucessful = writer.insert( table='raw.exposure_blocks', names=exposure_block.get_names(), values=exposure_block.get_values() )
    if not is_sucessful:
        print '[ISSUE] exposure_block'
        print '      errors: {0}'.format(misfit.errors)
        print '      file: {0}'.format(misfit.tarfile)
        print '      member: {0}'.format(misfit.tarmember)
    exposure_block.reset()
    return is_sucessful
    
def insert_event( basics, block_basics=None, daq_state='', block_uuid=None, pixels=[], byteblock={}, zerobias={} ):
    event.set_attributes( basics )
    event.set_block_attributes( block_basics, daq_state=daq_state )    
    event.set_block_uuid( block_uuid )
    event.set_pixels( pixels )
    event.set_byteblock( byteblock )
    event.set_zerobias( zerobias )    
    is_sucessful = writer.insert( table='raw.events', names=event.get_names(), values=event.get_values() )
    if not is_sucessful:
        print '[ISSUE] event'
        print '      errors: {0}'.format(misfit.errors)
        print '      file: {0}'.format(misfit.tarfile)
        print '      member: {0}'.format(misfit.tarmember)
    event.reset()
    return is_sucessful

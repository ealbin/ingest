"""DataChunk
deserialization, format enforcement and error checking.

functions
---------

from_string( string serialized message )
    Ingest serialized datachunk.
"""    

import crayfis_data_pb2

import ExposureBlock
import RunConfig
import CalibrationResult
import PreCalibrationResult

def from_string( serialized_chunk ):
    """Ingest serialized datachunk.
    
    Parameters
    ----------
    serialized_chunk : string
        Serialized protobuf DataChunk object
        
    Returns
    -------
    None
        maybe?
    """
    __debug_mode = False
        
    # deserialize protobuf DataChunk
    chunk = None
    try:
        chunk = crayfis_data_pb2.DataChunk.FromString( serialized_chunk )
        if __debug_mode: print '[DataChunk] DESERIALIZED protobuf string successfully'
    except Exception as e:
        # TODO: process error
        pass

    # break out members by type-category                         
    manifest = [ {'field':f, 'value':v} for [f,v] in chunk.ListFields() ]
    bytes    = [ m for m in manifest if m['field'].type == m['field'].TYPE_BYTES   ]
    messages = [ m for m in manifest if m['field'].type == m['field'].TYPE_MESSAGE ]
    enums    = [ m for m in manifest if m['field'].type == m['field'].TYPE_ENUM    ]
    basics   = [ m for m in manifest if m['field'].type in [ m['field'].TYPE_BOOL, 
                                                             m['field'].TYPE_FLOAT, m['field'].TYPE_DOUBLE,
                                                             m['field'].TYPE_INT32, m['field'].TYPE_SINT32, m['field'].TYPE_UINT32,
                                                             m['field'].TYPE_INT64, m['field'].TYPE_SINT64, m['field'].TYPE_UINT64,
                                                             m['field'].TYPE_STRING ] ]
    if __debug_mode: print '[DataChunk] FOUND {0} bytes, {1} messages, {2} enums and {3} basics'.format( len(bytes), len(messages), len(enums), len(basics) )

    # enforce expected structure
    if not len(manifest) - len(bytes) - len(messages) - len(enums) - len(basics) == 0:
        # TODO: error additional unknown data
        pass
    if not len( basics ) == 0:
        # TODO: err len( basics ) = {0} [!= 0]  format( len(basics) )
        pass
    if not len( bytes ) == 0:
        # TODO: err len( bytes ) = {0} [!= 0] format( len(bytes) )
        pass
    if not len( enums ) == 0:
        # TODO: err len( enums ) = {0} [!= 0] format( len(enums) )
        pass
    if len( messages ) == 0:
        # TODO: err len( messages ) = 0 [> 0]
        pass

    # TODO: maybe a good time to return if its a bust

    for message in messages:
        if message['field'].name == 'exposure_blocks':
            for block in message['value']:
                ExposureBlock.ingest(block)

        elif message['field'].name == 'run_configs':
            for config in message['value']:
                RunConfig.ingest(config)

        elif message['field'].name == 'calibration_results':                
            for result in message['value']:
                CalibrationResult.ingest(result)
                
        elif message['field'].name == 'precalibration_results':
            for result in message['value']:
                PreCalibrationResult.ingest(result)

        else:
            # TODO: err message type "{0}" is uknown   format(message['field'].name)
            pass

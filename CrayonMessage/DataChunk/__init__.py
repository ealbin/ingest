"""DataChunk
deserialization, format enforcement and error checking.

intended use:
-------------

    from_string( string serialized message, Cassandra football )
        Ingest serialized datachunk (update the football).
"""    

import crayfis_data_pb2

import ExposureBlock
import RunConfig
import CalibrationResult
import PreCalibrationResult

def from_string( serialized_chunk, football ):
    """Ingest serialized datachunk.
    
    Parameters
    ----------
    serialized_chunk : string
        Serialized protobuf DataChunk object
    
    football : dictionary
        Collection of Cassandra table name-value pairs representing the data.
        
    Returns
    -------
    None
        Implicitly updates the football and passes it.
    """
    __debug_mode = False
    
    # deserialize protobuf DataChunk
    chunk = None
    try:
        chunk = crayfis_data_pb2.DataChunk.FromString( serialized_chunk )
        if __debug_mode: print '[DataChunk] DESERIALIZED protobuf string successfully'
    except Exception as e:
        football.add_error( '[DataChunk] deserialization failure' )
        football.insert_misfit()
        return

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
        football.add_error( '[DataChunk] len(all) - len(expected) = {0} [!= 0]; '.format(len(manifest)-len(bytes)-len(messages)-len(enums)-len(basics)) )
    if not len( basics ) == 0:
        football.add_error( '[DataChunk] len(basics) = {0} [!= 0]; '.format(len(basics)) )
    if not len( bytes ) == 0:
        football.add_error( '[DataChunk] len(bytes) = {0} [!= 0]; '.format(len(bytes)) )
    if not len( enums ) == 0:
        football.add_error( '[DataChunk] len(enums) = {0} [!= 0]; '.format(len(enums)) )      
    if len( messages ) == 0:
        football.add_error( '[DataChunk] len(messages) = {0} [> 0]; '.format(len(messages)) )            

    if not football.get_n_errors() == 0:
        football.insert_misfit()
        return

    for message in messages:
        if message['field'].name == 'exposure_blocks':
            for block in message['value']:
                #ExposureBlock.ingest(block, football)
                pass

        elif message['field'].name == 'run_configs':
            for config in message['value']:
                if not RunConfig.ingest(config, football):
                    break

        elif message['field'].name == 'calibration_results':                
            for result in message['value']:
                if not CalibrationResult.ingest(result, football):
                    break
                
        elif message['field'].name == 'precalibration_results':
            for result in message['value']:
                if not PreCalibrationResult.ingest(result, football):
                    break

        else:
            football.add_error( '[DataChunk] message["field"].name = {0} [!= {exposure_blocks, run_configs, calibration_results, precalibration_results}]; '.format(message['field'].name) )
            football.insert_misfit()
            break

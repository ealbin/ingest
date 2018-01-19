"""ExposureBlock
deserialization, format enforcement and error checking.

intended use:
-------------

    ingest( google protobuf ExposureBlock object, Cassandra football )
        Ingest protobuf object (update the football).
"""    

import Event

def ingest( block, football ):
    """Ingest protobuf object.
    
    Parameters
    ----------
    block : google protobuf ExposureBlock
        ExposureBlock to be read
    
    football : Cassandra football object
        Interface to Cassandra
    
    Returns
    -------
    boolean
        True if sucessful, False if misfit behavior.
    """
    __debug_mode = False
    
    # break out members by type-category                         
    manifest = [ {'field':f, 'value':v} for [f,v] in block.ListFields() ]
    bytes    = [ m for m in manifest if m['field'].type == m['field'].TYPE_BYTES   ]
    messages = [ m for m in manifest if m['field'].type == m['field'].TYPE_MESSAGE ]
    enums    = [ m for m in manifest if m['field'].type == m['field'].TYPE_ENUM    ]
    basics   = [ m for m in manifest if m['field'].type in [ m['field'].TYPE_BOOL, 
                                                             m['field'].TYPE_FLOAT, m['field'].TYPE_DOUBLE,
                                                             m['field'].TYPE_INT32, m['field'].TYPE_SINT32, m['field'].TYPE_UINT32,
                                                             m['field'].TYPE_INT64, m['field'].TYPE_SINT64, m['field'].TYPE_UINT64,
                                                             m['field'].TYPE_STRING ] ]
    if __debug_mode: print '[ExposureBlock] FOUND {0} bytes, {1} messages, {2} enums and {3} basics'.format( len(bytes), len(messages), len(enums), len(basics) )

    # enforce expected structure
    if not len(manifest) - len(bytes) - len(messages) - len(enums) - len(basics) == 0:
        football.add_error( '[ExposureBlock] len(all) - len(expected) = {0} [!= 0]; '.format(len(manifest)-len(bytes)-len(messages)-len(enums)-len(basics)) )
    if not len( bytes ) == 0:
        football.add_error( '[ExposureBlock] len(bytes) = {0} [!= 0]; '.format(len(bytes)) )
    if not len( enums ) == 1:
        football.add_error( '[ExposureBlock] len(enums) = {0} [!= 1]; '.format(len(enums)) )  
    if not enums[0]['field'].name == 'daq_state':
        football.add_error( '[ExposureBlock] enums[0]["field"].name = {0} [!= "daq_state"]; '.format(enums[0]['field'].name) )

    # translate enum into string
    state = ''
    if   enums[0]['value'] == 0:
        state = 'INIT'
    elif enums[0]['value'] == 1:
        state = 'CALIBRATION'
    elif enums[0]['value'] == 2:
        state = 'DATA'
    elif enums[0]['value'] == 3:
        state = 'PRECALIBRATION'
    else:
        football.add_error( '[ExposureBlock] daq_state = {0} [!= {0,1,2,3}]; '.format(enums[0]['value']) )

    # collect event_ids
    event_ids = []
    for message in messages:
        if message['field'].name == 'events':
            for event in message['value']:
                # save event to Cassandra
                if not Event.ingest( event, football ):
                    football.add_error( '[ExposureBlock] bad event' )
                    continue
                event_ids.append( football.get_event_uuid() )
        else:
            football.add_error( '[ExposureBlock] message["field"].name = {0} [!= {events, byteblocks, zerobiassquares}]; '.format(message['field'].name) )

    # save exposure_block to Cassandra
    if not football.insert_exposure_block( basics, daq_state=state, event_ids=event_ids ):
        football.add_error( '[ExposureBlock] field name missmatch: {0}'.format([b['field'].name for b in basics]) )

    if not football.get_n_errors() == 0:
        return False
    return True

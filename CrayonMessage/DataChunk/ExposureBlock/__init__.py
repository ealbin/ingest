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
    
    football : dictionary
        Collection of Cassandra table name-value pairs representing the data.
    
    Returns
    -------
    None
        Implicitly updates the football.
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
        football['error_string'] += '[ExposureBlock] len(all) - len(expected) = {0} [!= 0]; '.format(len(manifest)-len(bytes)-len(messages)-len(enums)-len(basics))
    if not len( bytes ) == 0:
        football['error_string'] += '[ExposureBlock] len(bytes) = {0} [!= 0]; '.format(len(bytes))
    if not len( enums ) == 1:
        football['error_string'] += '[ExposureBlock] len(enums) = {0} [!= 1]; '.format(len(enums))    
    if not enums[0]['field'].name == 'daq_state':
        football['error_string'] += '[ExposureBlock] enums[0]["field"].name = {0} [!= "daq_state"]; '.format(enums[0]['field'].name)

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
        football['error_string'] += '[ExposureBlock] daq_state = {0} [!= {0,1,2,3}]; '.format(enums[0]['value'])

    football['exposure_blocks'].append( { 'header':basics, 'daq_state':state, 'events':[] } )
    
    for message in messages:
        if message['field'].name == 'events':
            for event in message['value']:
                Event.ingest( event, football )
        else:
            football['error_string'] += '[ExposureBlock] message["field"].name = {0} [!= {events, byteblocks, zerobiassquares}]; '.format(message['field'].name)


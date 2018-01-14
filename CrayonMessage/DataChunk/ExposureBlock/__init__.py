"""ExposureBlock
deserialization, format enforcement and error checking.

functions
---------

ingest( google protobuf ExposureBlock object )
    Ingest protobuf object into a python dictionary.
"""    

import Event
import ByteBlock
import ZeroBiasSquare

def ingest( block ):
    """Ingest protobuf object into a python dictionary.
    
    Parameters
    ----------
    block : google protobuf ExposureBlock
        ExposureBlock to be read
    
    Returns
    -------
    None
        maybe?
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
        # TODO: error additional unknown data
        pass
    if not len( bytes ) == 0:
        # TODO: err len( bytes ) = {0} [!= 0] format( len(bytes) )
        pass
    if not len( enums ) == 1:
        # TODO: err len( enums ) = {0} [!= 1] format( len(enums) )
        pass
    if not enums[0]['field'].name == 'daq_state':
        # TODO: err "{0}" [!= "daq_state"] format( enums[0]['field'].name )
        pass

    v = ''
    if   enums[0]['value'] == 0:
        v = 'INIT'
    elif enums[0]['value'] == 1:
        v = 'CALIBRATION'
    elif enums[0]['value'] == 2:
        v = 'DATA'
    elif enums[0]['value'] == 3:
        v = 'PRECALIBRATION'
    else:
        # TODO: err daq_state {0} unknown [!={0,1,2,3}] format( enums[0]['value'] )
        pass

    # TODO: append or update enums
    # e.g. enums[0]['value'] = v
    # e.g. basics['daq_state'] = v

    for message in messages:
        if not message['field'].name == 'events':
            # TODO: err unknown subfield "{0}" [!= "events"] format(message['field'].name)
            continue

        for event in message['value']:
            Event.ingest( event )

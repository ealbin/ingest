"""CrayonMessage
deserialization, format enforcement and error checking.

intended use:
-------------

    from_msg( tarfile.ExFileObject serialized message, Cassandra football  )
        Ingest extracted message (update the football).
"""

import crayfis_data_pb2
import DataChunk

def from_msg( serialized_msg, football ):
    """Ingest extracted message.
    
    Parameters
    ----------
    serialized_msg : tarfile.ExFileObject
        Serialized raw object from tarfile.extractfile( message ).
    
    football : dictionary
        Collection of Cassandra table name-value pairs representing the data.
 
    Returns
    -------
    None
        Implicitly updates the football and passes it.
    """
    __debug_mode = False
    
    # deserialize protobuf CrayonMessage
    protobuf_msg = None
    try:
        serialized_msg.seek(0)
        serialized_string = serialized_msg.read()
        football['raw_string'] = serialized_string
        protobuf_msg = crayfis_data_pb2.CrayonMessage.FromString( serialized_string )
        if __debug_mode: print '[CrayonMessage] DESERIALIZED protobuf string successfully'
    except Exception as e:
        football['error_string'] += '[CrayonMessage] deserialization failure; '
        return
                         
    # break out members by type-category                         
    manifest = [ {'field':f, 'value':v} for [f,v] in protobuf_msg.ListFields() ]
    bytes    = [ m for m in manifest if m['field'].type == m['field'].TYPE_BYTES   ]
    messages = [ m for m in manifest if m['field'].type == m['field'].TYPE_MESSAGE ]
    enums    = [ m for m in manifest if m['field'].type == m['field'].TYPE_ENUM    ]
    basics   = [ m for m in manifest if m['field'].type in [ m['field'].TYPE_BOOL, 
                                                             m['field'].TYPE_FLOAT, m['field'].TYPE_DOUBLE,
                                                             m['field'].TYPE_INT32, m['field'].TYPE_SINT32, m['field'].TYPE_UINT32,
                                                             m['field'].TYPE_INT64, m['field'].TYPE_SINT64, m['field'].TYPE_UINT64,
                                                             m['field'].TYPE_STRING ] ]
    if __debug_mode: print '[CrayonMessage] FOUND {0} bytes, {1} messages, {2} enums and {3} basics'.format( len(bytes), len(messages), len(enums), len(basics) )
    
    # enforce expected structure
    if not len(manifest) - len(bytes) - len(messages) - len(enums) - len(basics) == 0:
        football['error_string'] += '[CrayonMessage] len(all) - len(expected) = {0} [!= 0]; '.format(len(manifest)-len(bytes)-len(messages)-len(enums)-len(basics))
    if not len( messages ) == 0:
        football['error_string'] += '[CrayonMessage] len(messages) = {0} [!= 0]; '.format(len(messages))
    if not len( enums ) == 0:
        football['error_string'] += '[CrayonMessage] len(enums) = {0} [!= 0]; '.format(len(enums))    
    if not len( bytes ) == 1:
        football['error_string'] += '[CrayonMessage] len(bytes) = {0} [!= 1]; '.format(len(bytes))        
    if not bytes[0]['field'].name == 'payload':
        football['error_string'] += '[CrayonMessage] bytes[0]["field"].name = {0} [!= "payload"]; '.format(bytes[0]['field'].name)

    if not len( football['error_string'] ) == 0:
        return

    football['crayon_message'] = basics
        
    # deserialize protobuf datachunk
    DataChunk.from_string( bytes[0]['value'], football )

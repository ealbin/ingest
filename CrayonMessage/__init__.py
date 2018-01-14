"""CrayonMessage
deserialization, format enforcement and error checking.

functions
---------

from_msg( tarfile.ExFileObject serialized message  )
    Ingest extracted message.
"""

import crayfis_data_pb2
import DataChunk

def from_msg( serialized_msg ):
    """Ingest extracted message.
    
    Parameters
    ----------
    serialized_msg : tarfile.ExFileObject
        Serialized raw object from tarfile.extractfile( message ).
    
    Returns
    -------
    None
        maybe?
    """
    __debug_mode = False
    
    # deserialize protobuf CrayonMessage
    protobuf_msg = None
    try:
        serialized_msg.seek(0)
        protobuf_msg = crayfis_data_pb2.CrayonMessage.FromString( serialized_msg.read() )
        if __debug_mode: print '[CrayonMessage] DESERIALIZED protobuf string successfully'
    except Exception as e:
        # TODO: process error
        pass
                         
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
        # TODO: error additional unknown data
        pass
    if not len( messages ) == 0:
        # TODO: err len( messages ) = {0} [!= 0]  format( len(messages) )
        pass
    if not len( enums ) == 0:
        # TODO: err len( enums ) = {0} [!= 0] format( len(enums) )
        pass
    if not len( bytes ) == 1:
        # TODO: err len( bytes ) = {0} [!= 1] format( len(bytes) )
        pass
    if not bytes[0]['field'].name == 'payload':
        # TODO: err bytes[0]['field'].name = {0} [!= "payload"] format( bytes[0]['field'].name )
        pass

    # deserialize protobuf datachunk
    DataChunk.from_string( bytes[0]['value'] )

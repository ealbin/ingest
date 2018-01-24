"""Event
deserialization, format enforcement and error checking.

inteded use:
------------

    ingest( google protobuf Event object, Cassandra football )
        Ingest protobuf object (updates the football).
"""

import ByteBlock
import Pixel
import ZeroBiasSquare

def ingest( event, football ):
    """Ingest protobuf object.
    
    Parameters
    ----------
    event : google protobuf Event
        Event to be read
        
    football : Cassandra football object
        Cassandra interface.
        
    Returns
    -------
    boolean
        True if sucessful, False if misfit behavior.
    """
    __debug_mode = False

    # break out members by type-category                         
    manifest = [ {'field':f, 'value':v} for [f,v] in event.ListFields() ]
    bytes    = [ m for m in manifest if m['field'].type == m['field'].TYPE_BYTES   ]
    messages = [ m for m in manifest if m['field'].type == m['field'].TYPE_MESSAGE ]
    enums    = [ m for m in manifest if m['field'].type == m['field'].TYPE_ENUM    ]
    basics   = [ m for m in manifest if m['field'].type in [ m['field'].TYPE_BOOL, 
                                                             m['field'].TYPE_FLOAT, m['field'].TYPE_DOUBLE,
                                                             m['field'].TYPE_INT32, m['field'].TYPE_SINT32, m['field'].TYPE_UINT32,
                                                             m['field'].TYPE_INT64, m['field'].TYPE_SINT64, m['field'].TYPE_UINT64,
                                                             m['field'].TYPE_STRING ] ]
    if __debug_mode: print '[Event] FOUND {0} bytes, {1} messages, {2} enums and {3} basics'.format( len(bytes), len(messages), len(enums), len(basics) )

    # enforce expected structure
    if not len(manifest) - len(bytes) - len(messages) - len(enums) - len(basics) == 0:
        football.add_error( '[Event] len(all) - len(expected) = {0} [!= 0]; '.format(len(manifest)-len(bytes)-len(messages)-len(enums)-len(basics)) )
    if not len( bytes ) == 0:
        football.add_error( '[Event] len(bytes) = {0} [!= 0]; '.format(len(bytes)) )
    if not len( enums ) == 0:
        football.add_error( '[Event] len(enums) = {0} [!= 0]; '.format(len(enums)) )  

    pixels    = []
    byteblock = None
    zerobias  = None
    for message in messages:
        if message['field'].name == 'pixels':
            for pixel in message['value']:
                pixels.append( Pixel.ingest(pixel, football) )
        
        elif message['field'].name == 'byteblocks':
            for byteblock in message['value']:
                if byteblock is not None:
                    football.add_error( '[Event] too many byteblocks' )
                else:
                    byteblock = ByteBlock.ingest(byteblock, football)
                
        elif message['field'].name == 'zerobiassquares':
            for square in message['value']:
                if zerobias is not None:
                    football.add_error( '[Event] too many zero-bias squares' )
                else:
                    zerobias = ZeroBiasSquare.ingest(square, football)
                            
        else:
            football.add_error( '[Event] message["field"].name = {0} [!= {pixels, byteblocks, zerobiassquares}]; '.format(message['field'].name) )

    if not football.get_n_errors():
        return False
        
    # save event to Cassandra
    if not football.insert_event( basics, pixels=pixels, byteblock=byteblock, zerobias=zerobias ):
        football.add_error( '[Event] field name missmatch: {0}'.format([b['field'].name for b in basics]) )

    if not football.get_n_errors():
        return False
    return True

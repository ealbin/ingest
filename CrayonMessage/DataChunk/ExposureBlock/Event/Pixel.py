"""Pixel
deserialization, format enforcement and error checking.

inteded use:
------------

    ingest( google protobuf Pixel object, Cassandra football )
        Ingest protobuf object (updates the football).
"""

def ingest( pixel, football ):
    """Ingest protobuf object.
    
    Parameters
    ----------
    pixel : google protobuf Pixel
        Pixel to be read
        
    football : Cassandra football object
        Cassandra interface.
        
    Returns
    -------
    python dictionary
        name : value pairs of pixel
    """
    __debug_mode = False

    # break out members by type-category                         
    manifest = [ {'field':f, 'value':v} for [f,v] in pixel.ListFields() ]
    bytes    = [ m for m in manifest if m['field'].type == m['field'].TYPE_BYTES   ]
    messages = [ m for m in manifest if m['field'].type == m['field'].TYPE_MESSAGE ]
    enums    = [ m for m in manifest if m['field'].type == m['field'].TYPE_ENUM    ]
    basics   = [ m for m in manifest if m['field'].type in [ m['field'].TYPE_BOOL, 
                                                             m['field'].TYPE_FLOAT, m['field'].TYPE_DOUBLE,
                                                             m['field'].TYPE_INT32, m['field'].TYPE_SINT32, m['field'].TYPE_UINT32,
                                                             m['field'].TYPE_INT64, m['field'].TYPE_SINT64, m['field'].TYPE_UINT64,
                                                             m['field'].TYPE_STRING ] ]
    if __debug_mode: print '[Pixel] FOUND {0} bytes, {1} messages, {2} enums and {3} basics'.format( len(bytes), len(messages), len(enums), len(basics) )

    # enforce expected structure
    if not len(manifest) - len(bytes) - len(messages) - len(enums) - len(basics) == 0:
        football.add_error( '[Pixel] len(all) - len(expected) = {0} [!= 0]; '.format(len(manifest)-len(bytes)-len(messages)-len(enums)-len(basics)) )
    if not len( bytes ) == 0:
        football.add_error( '[Pixel] len(bytes) = {0} [!= 0]; '.format(len(bytes)) )
    if not len( enums ) == 0:
        football.add_error( '[Pixel] len(enums) = {0} [!= 0]; '.format(len(enums)) )
    if not len( messages ) == 0:
        football.add_error( '[Pixel] len(messages) = {0} [!= 0]; '.format(len(messages)) )

    # build dictionary
    pdict = { 'x':None, 'y':None, 'val':None, 'adjusted_val':None, 'near_max':None, 'avg_3':None, 'avg_5':None }
    for basic in basics:
        if basic['field'].name not in pdict.keys():
            football.add_error( '[Pixel] unknown attribute: {0}'.format(basic['field'].name) )
            continue
        pdict[ basic['field'].name ] = basic['value']
    
    return pdict

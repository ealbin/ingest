"""ZeroBiasSquare
deserialization, format enforcement and error checking.

functions
---------

ingest( google protobuf ZeroBiasSquare object )
    Ingest protobuf object into a python dictionary.
"""

def ingest( square, football ):
    """Ingest protobuf object into a python dictionary.
    
    Parameters
    ----------
    square : google protobuf ZeroBiasSquare
        Calibration to be read
        
    football : dictionary
        Collection of column name-value pairs representing the data.
            
    Returns
    -------
    None
        Implicitly updates the football.
    """
    __debug_mode = True
        
    # break out members by type-category                         
    manifest = [ {'field':f, 'value':v} for [f,v] in square.ListFields() ]
    bytes    = [ m for m in manifest if m['field'].type == m['field'].TYPE_BYTES   ]
    messages = [ m for m in manifest if m['field'].type == m['field'].TYPE_MESSAGE ]
    enums    = [ m for m in manifest if m['field'].type == m['field'].TYPE_ENUM    ]
    basics   = [ m for m in manifest if m['field'].type in [ m['field'].TYPE_BOOL, 
                                                             m['field'].TYPE_FLOAT, m['field'].TYPE_DOUBLE,
                                                             m['field'].TYPE_INT32, m['field'].TYPE_SINT32, m['field'].TYPE_UINT32,
                                                             m['field'].TYPE_INT64, m['field'].TYPE_SINT64, m['field'].TYPE_UINT64,
                                                             m['field'].TYPE_STRING ] ]
    if __debug_mode: print '[ZeroBiasSquare] FOUND {0} bytes, {1} messages, {2} enums and {3} basics'.format( len(bytes), len(messages), len(enums), len(basics) )

    # enforce expected structure
    if not len(manifest) - len(bytes) - len(messages) - len(enums) - len(basics) == 0:
        football['error_string'] += '[ZeroBiasSquare] len(all) - len(expected) = {0} [!= 0]; '.format(len(manifest)-len(bytes)-len(messages)-len(enums)-len(basics))
    if not len( bytes ) == 0:
        football['error_string'] += '[ZeroBiasSquare] len(bytes) = {0} [!= 0]; '.format(len(bytes))
    if not len( enums ) == 0:
        football['error_string'] += '[ZeroBiasSquare] len(enums) = {0} [!= 0]; '.format(len(enums))    
    if not len( messages ) == 0:
        football['error_string'] += '[ZeroBiasSquare] len(messages) = {0} [!= 0]; '.format(len(messages))        
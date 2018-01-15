"""CalibrationResult
deserialization, format enforcement and error checking.

intended use:
-------------

    ingest( google protobuf CalibrationResult object, Cassandra football )
        Ingest protobuf object (update the football).
"""

def ingest( result, football ):
    """Ingest protobuf object.
    
    Parameters
    ----------
    result : google protobuf CalibrationResult
        Calibration to be read
        
    football : dictionary
        Collection of Cassandra table name-value pairs representing the data.
        
    Returns
    -------
    None
        Implicitly updates the football.
    """
    __debug_mode = False
        
    # break out members by type-category                         
    manifest = [ {'field':f, 'value':v} for [f,v] in result.ListFields() ]
    bytes    = [ m for m in manifest if m['field'].type == m['field'].TYPE_BYTES   ]
    messages = [ m for m in manifest if m['field'].type == m['field'].TYPE_MESSAGE ]
    enums    = [ m for m in manifest if m['field'].type == m['field'].TYPE_ENUM    ]
    basics   = [ m for m in manifest if m['field'].type in [ m['field'].TYPE_BOOL, 
                                                             m['field'].TYPE_FLOAT, m['field'].TYPE_DOUBLE,
                                                             m['field'].TYPE_INT32, m['field'].TYPE_SINT32, m['field'].TYPE_UINT32,
                                                             m['field'].TYPE_INT64, m['field'].TYPE_SINT64, m['field'].TYPE_UINT64,
                                                             m['field'].TYPE_STRING ] ]
    if __debug_mode: print '[CalibrationResult] FOUND {0} bytes, {1} messages, {2} enums and {3} basics'.format( len(bytes), len(messages), len(enums), len(basics) )

    # enforce expected structure
    if not len(manifest) - len(bytes) - len(messages) - len(enums) - len(basics) == 0:
        football['error_string'] += '[CalibrationResult] len(all) - len(expected) = {0} [!= 0]; '.format(len(manifest)-len(bytes)-len(messages)-len(enums)-len(basics))
    if not len( bytes ) == 0:
        football['error_string'] += '[CalibrationResult] len(bytes) = {0} [!= 0]; '.format(len(bytes))
    if not len( enums ) == 0:
        football['error_string'] += '[CalibrationResult] len(enums) = {0} [!= 0]; '.format(len(enums))    
    if not len( messages ) == 0:
        football['error_string'] += '[CalibrationResult] len(messages) = {0} [!= 0]; '.format(len(messages))        
    
    football['calibration_results'].append(basics)

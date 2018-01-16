"""Cassandra football interface

inteded use:
------------

    get_football()
        The football is a python dictionary mapping the
        names of Cassandra table columns to their respective values.
        It gets passed between functions and updated with ingested data
        as it travels.
        
    write_football()
        Called when the football is ready to be written to Cassandra.
        Football is preserved in the write operation, to clean call
        get_football(clean=True).        
"""

# TODO: import things

class __CassandraFootball:

    _error_string           = None
    _n_errors               = 0
    _metadata               = None
    _serialized_message     = None
    
    _headers                = None
    _exposure_blocks        = None
    _run_configs            = None
    _calibration_results    = None
    _precalibration_results = None
    
    def clean(self):
        _error_string           = None
        _n_errors               = 0

        _metadata.clear()
        _serialized_message.clear()
        
        _headers.clear()
        _exposure_blocks.clear()
        _events.clear()
        _run_configs.clear()
        _calibration_results.clear()
        _precalibration_results.clear()
        

        _metadata               = {'columns':[], 'values':[]}
        _serialized_message     = {'columns':[], 'values':[]}
        
        _headers                = {'columns':[], 'values':[]}
        _exposure_blocks        = {'columns':[], 'values':[]}
        _events                 = {'columns':[], 'values':[]}
        _run_configs            = {'columns':[], 'values':[]}
        _calibration_results    = {'columns':[], 'values':[]}
        _precalibration_results = {'columns':[], 'values':[]}
        
    def __init__(self):
        self.clean()

    def add_error(self, error):
        _delimiter = '; '
        if _error_string is None:
            _error_string = str(error)
        else:
            _error_string += _delimiter + str(error)
        _n_errors += 1
            
    def n_errors(self):
        return _n_errors
            
    def add_metadata(self, host='', filepath='', msg_name=''):
        _metadata = { 'columns' : ['host', 'filepath', 'msg_name' ],
                      'values'  : [ host,    filepath,  msg_name  ]  }
        
    def add_serialized(self, message):
        # add Cassandra escape character ' for blob storage
        # repr() to prevent escape character evaluation in python
        _serialized_message = { 'columns' : [ 'serialized_message' ],
                                'values'  : [ repr(message)[1:-1].replace("'", "''") ] }

    def add_headers( headers ):
        _allowed = 
        _headers = {}
        for h in headers:
            if h['field'].type == h['field'].STRING

        _headers = headers

    def add_exposure_block( block ):
    def add_event_to_block( event ):
    def add_pixel_to_event( pixel ):
    def add_zbias_to_event( zerobias ):
    def add_byteb_to_event( byteblock ):
    
    def add_runconfig( config ):
    def add_calibration_result( result ):
    def add_precalibration_result( result ):
    
    

__football = __CassandraFootball()

def get_football(clean=False):
    """returns dictionary football
    """
    if clean:
        __football.clean()
    return __football

def write_football():
    """write football to Cassandra
    """
    global __football
    if not len(__football['error_string']) == 0:
        print __football['error_string']
    else:
        for [k, v] in __football.viewitems():
            print '{0}_____: {1}'.format( k.upper(), repr(v)[:1000] )
        print '\n\n'    
#        print __football['crayon_message']
#        print __football['exposure_blocks']
#        print __football['run_configs']
#        print __football['calibration_results']
#        print __football['precalibration_results']
#    for [f,v] in __football.viewitems():
#        print f, v

__clean_football()

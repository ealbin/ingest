"""Football stuff
"""

# TODO: import things

__football = {}

def __clean_football():
    global __football
    del __football
    
    __football                           = {}
    __football['error_string']           = ''
    __football['exposure_blocks']        = []
    __football['run_configs']            = []
    __football['calibration_results']    = []
    __football['precalibration_results'] = []

def get_football(clean=False):
    """returns dictionary football
    """
    global __football
    if clean:
        __clean_football()
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

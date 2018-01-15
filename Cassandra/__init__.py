"""Football stuff
"""

# TODO: import things

__football = {}
__football['error_string'] = ''

def get_football(clean=False):
    """returns dictionary football
    """
    global __football
    if clean:
        del __football
        __football = {}
        __football['error_string'] = ''
    return __football

def write_football():
    """write football to Cassandra
    """
    global __football
    if not len(__football['error_string']) == 0:
        print __football['error_string']
#    for [f,v] in __football.viewitems():
#        print f, v

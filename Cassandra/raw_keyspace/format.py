"""Format conversion for Cassandra data types
"""

def varchar( varchar ):
    string = repr(varchar)
    if string[0].lower() == 'u':
        string = string[2:-1]
    else:
        string = string[1:-1]
    return "'{0}'".format( string.replace("'","''") )
    
def inet( inet ):
    return varchar( inet )
        
def blob( blob ):
    return 'textAsBlob({0})'.format( varchar( blob ) )    

def boolean( boolean ):
    return str(boolean).lower()

def set_numeric( array ):
    string = '{ '
    for a in array:
        string += str(a) + ', '
    string.rstrip(', ')
    string += ' }'
    return string

def byte_block( block ):
    # TODO: this
    return '' 

def zero_bias( square ):
    # TODO: this
    return ''
    
def pixels( pixels ):
    # TODO: this
    return ''
    
    
# pixel type def
#x               varint
#y               varint
#val             varint
#adjusted_val    varint
#near_max        varint
#ave_3           double
#ave_5           double

# square type def
#x_min           varint
#y_min           varint
#val             varint
#frame_number    varint 

# byteblock type def
#x               set<varint>
#y               set<varint>
#val             set<varint>
#side_length     varint 

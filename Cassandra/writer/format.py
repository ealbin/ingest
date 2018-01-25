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
    string = string[:-2] + ' }'
    return string

def byte_block( block ):
    string  = '{ '
    if 'x'           in block: string += 'x: {0}, '.format( set_numeric( block['x'] ) )
    if 'y'           in block: string += 'y: {0}, '.format( set_numeric( block['y'] ) )
    if 'val'         in block: string += 'val: {0}, '.format( set_numeric( block['val'] ) ) 
    if 'side_length' in block: string += 'side_length: {0}, '.format( block['side_length'] )
    string = string[:-2] + ' }'
    return string

def zero_bias( square ):
    string  = '{ '
    if 'x_min'        in square: string += 'x_min: {0}, '.format( square['x_min'] )
    if 'y_min'        in square: string += 'y_min: {0}, '.format( square['y_min'] ) 
    if 'val'          in square: string += 'val: {0}, '.format( square['val'] )
    if 'frame_number' in square: string += 'frame_number: {0}, '.format( square['frame_number'] )
    string = string[:-2] + ' }'
    return string

def pixels( pixels ):
    string = '{ '
    for n, pixel in enumerate(pixels):
        string += '{ '
        
        if 'x'            in pixel: string += 'x: {0}, '.format( pixel['x'] )
        if 'y'            in pixel: string += 'y: {0}, '.format( pixel['y'] )
        if 'val'          in pixel: string += 'val: {0}, '.format( pixel['val'] )
        if 'adjusted_val' in pixel: string += 'adjusted_val: {0}, '.format( pixel['adjusted_val'] )
        if 'near_max'     in pixel: string += 'near_max: {0}, '.format( pixel['near_max'] )
        if 'ave_3'        in pixel: string += 'ave_3: {0}, '.format( pixel['ave_3'] )
        if 'ave_5'        in pixel: string += 'ave_5: {0}, '.format( pixel['ave_5'] )
        string = string[:-2] + ' }, '
    string = string[:-2] + ' }'
    return string

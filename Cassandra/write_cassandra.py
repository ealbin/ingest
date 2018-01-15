#!/bin/env python

# drop run_id from header
# daq_state  enum: INIT=0, CALIBRATION=1, DATA=2, PRECALIBRATION=3

import unpack

from cassandra_session import get_session
session = get_session()

# raw_message is an extracted tarfile object
def write_message( raw_message, metadata ):

    message = unpack.raw_message( raw_message, metadata )
    
    if not message['is_good']:
        # add to isle of misfit messages
        return False

    # load columns and values from message to write
    columns = ''
    values  = ''
    # header
    for h in message['data']['header']:
        columns += h['name']  + ', '
        v = '{0}'.format( h['value'] )
        if ( h['name'] == 'device_id' or
             h['name'] == 'app_code'  or
             h['name'] == 'remote_addr' ):
             v = "'{0}'".format(v)
        values  += v + ', '

    # gymnastics to make serialized payload cassandra compatable    
    payload    = repr( message['data']['payload'] )[1:-1]
    armed_load = "textAsBlob( '{0}' )".format( payload.replace("'","''") )

    columns += 'payload'
    values  += armed_load
    command  = """INSERT INTO raw.message ( {0} ) VALUES ( {1} ) IF NOT EXISTS;""".format( columns, values )

    try:
        session.execute( command )
    except Exception, e:
        length     = len(armed_load)
        dollars    = armed_load.count('$')
        ddollars   = armed_load.count('$$')
        singles    = armed_load.count("'")
        doubles    = armed_load.count('"')
        ats        = armed_load.count('@')
        print 'payload debug: $:{0}\t$$:{1}\t\':{2}\t":{3}\t@:{4}\tlen:{5}'.format(dollars,ddollars,singles,doubles,ats,length)

        index = int( str(e).split(':')[2].split(' ')[0] )
        char  = str(e).split('"')[-2].split(' ')[-1][:10]
        print 'err 12 : failed to insert, command index {0} involving "{1}", trouble spot: "...{2}                    '.format(index, char, command[index-10:index-1] + ' ' + command[index] + ' ' + command[index+1:index+10] + '..."')
        print '\n'
        # this is a bad place to be
        return False
                       
    return True




"""Cassandra data ingestion module

intended use:
-------------

    ingest.from_tarfile( filepath ) 
        Ingest CrayonMessages from file.tar.gz into Cassandra
"""

import os
import tarfile
import CrayonMessage
import Cassandra


def from_tarfile( filepath ):
    """Ingest a Crayfis tarfile into Cassandra.
    
    Parameters
    ----------
    filepath : string
        Full system filepath locating data tarfile, 
        e.g. /data/daq.crayfis.io/raw/YYYY/MM/HOST/HH.tar.gz
        
    Returns
    -------
    None
        Writes data contained in filepath to Cassandra
    """
    __debug_mode = True
    __debug_N    = 1000
    
    # load tarfile into memory
    try:
        crayfile = tarfile.open( filepath, 'r:gz' )
        if __debug_mode: print 'LOADED tarfile successfully: {0}'.format(crayfile.name)
    except Exception as e:
        print 'terminal error: {0} cannot be found/opened.'.format(filepath)
        return
                
    craymsgs = [ m for m in crayfile.getmembers() if m.name.endswith('.msg') ]
    if __debug_mode: print 'FOUND {0} messages'.format(len(craymsgs))

    host = os.uname()
    football = Cassandra.get_football()

    for msg_i, message in enumerate(craymsgs):
        Cassandra.clear_football()
        football.set_metadata(host=host, tarfile=filepath, tarmember=message.name)

        msg = crayfile.extractfile( message )
        CrayonMessage.from_msg( msg, football )
        msg.close()

        if __debug_mode and msg_i == __debug_N - 1 : print 'DEBUG break after {0} messages'.format(__debug_N); break
            
    crayfile.close()


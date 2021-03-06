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
    boolean
        Writes data contained in filepath to Cassandra and returns true.
        If there was a problem that couldn't be dealt with, returns false.
    """
    __debug_mode = False
    __debug_N    = 100
    
    # load tarfile into memory
    try:
        crayfile = tarfile.open( filepath, 'r:gz' )
        if __debug_mode: print 'LOADED tarfile successfully: {0}'.format(crayfile.name)
    except Exception as e:
        print 'terminal error: {0} cannot be found/opened.'.format(filepath)
        return False
                
    craymsgs = [ m for m in crayfile.getmembers() if m.name.endswith('.msg') ]
    if __debug_mode: print 'FOUND {0} messages'.format(len(craymsgs))

    host = os.uname()
    football = Cassandra.get_football()
    for msg_i, message in enumerate(craymsgs):
        football.clear()
        # save metadata
        if not football.set_metadata(host=host, tarfile=filepath, tarmember=message.name):
            football.add_error( '[ingest] metadata failure, check attribute names ingest/Cassandra/[keyspace]/[table].py' )
            football.insert_misfit()
            continue # abort this one, go to next message

        msg = crayfile.extractfile( message )
        # save message to Cassandra
        CrayonMessage.from_msg( msg, football )
        msg.close()

        if __debug_mode and msg_i == __debug_N - 1 : print 'DEBUG break after {0} messages'.format(__debug_N); break
    crayfile.close()
    return True

"""Cassandra data ingestion.

ingest.from_tarfile( filepath ) 
"""

import tarfile

import CrayonMessage

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
        I think it will just be write to Cassandra...(?)
    """
    __debug_mode = True
    
    try:
        crayfile = tarfile.open( filepath, 'r:gz' )
        if __debug_mode: print 'LOADED tarfile successfully: {0}'.format(crayfile.name)
    except Exception as e:
        # TODO: process error
        pass
                
    craymsgs = [ m for m in crayfile.getmembers() if m.name.endswith('.msg') ]
    if __debug_mode: print 'FOUND {0} messages'.format(len(craymsgs))

    for msg_i, message in enumerate(craymsgs):
        # TODO: metadata = host, filepath, message.name
        msg = crayfile.extractfile( message )
        CrayonMessage.from_msg( msg )
        msg.close()
        # TODO: write cassandra
        if __debug_mode and msg_i == 9 : print 'DEBUG break after 10 messages'; break
            
    crayfile.close()

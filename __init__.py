"""Cassandra data ingestion module

intended use:
-------------

    ingest.from_tarfile( filepath ) 
        Ingest CrayonMessages from file.tar.gz into Cassandra
"""

import ingest

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
        Writes data contained in filepath to Cassandra and returns True.
        Returns False if a non-recoverable error occurs
    """
    return ingest.from_tarfile( filepath )

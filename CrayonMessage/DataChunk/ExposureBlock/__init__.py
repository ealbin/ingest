"""ExposureBlock
deserialization, format enforcement and error checking.

intended use:
-------------

    ingest( google protobuf ExposureBlock object, Cassandra football )
        Ingest protobuf object (update the football).
"""    

import ExposureBlock

def ingest( block, football ):
    """Ingest protobuf object.
    
    Parameters
    ----------
    block : google protobuf ExposureBlock
        ExposureBlock to be read
    
    football : Cassandra football object
        Interface to Cassandra
    
    Returns
    -------
    boolean
        True if sucessful, False if misfit behavior.
    """
    return ExposureBlock.ingest( block, football )

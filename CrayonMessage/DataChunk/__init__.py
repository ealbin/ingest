"""DataChunk
deserialization, format enforcement and error checking.

intended use:
-------------

    from_string( string serialized message, Cassandra football )
        Ingest serialized datachunk (update Cassandra via the football).
"""    

import DataChunk

def from_string( serialized_chunk, football ):
    """Ingest serialized datachunk.
    
    Parameters
    ----------
    serialized_chunk : string
        Serialized protobuf DataChunk object
    
    football : Cassandra football object
        Interface to Cassandra that gets passed around.
        
    Returns
    -------
    None
        Updates Cassandra via the football, and then passes it.
    """
    DataChunk.from_string( serialized_chunk, football )

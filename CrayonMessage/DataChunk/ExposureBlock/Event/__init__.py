"""Event
deserialization, format enforcement and error checking.

inteded use:
------------

    ingest( google protobuf Event object, Cassandra football )
        Ingest protobuf object (updates the football).
"""

import Event

def ingest( event, football, block_basics=None, daq_state=None, block_uuid=None ):
    """Ingest protobuf object.
    
    Parameters
    ----------
    event : google protobuf Event
        Event to be read
        
    football : Cassandra football object
        Cassandra interface.
        
    Returns
    -------
    boolean
        True if sucessful, False if misfit behavior.
    """
    return Event.ingest( event, football, block_basics=block_basics, daq_state=daq_state, block_uuid=block_uuid )

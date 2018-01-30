"""CrayonMessage
deserialization, format enforcement and error checking.

intended use:
-------------

    from_msg( tarfile.ExFileObject serialized message, Cassandra football  )
        Ingest crayon message (and update the football).
"""

import CrayonMessage

def from_msg( serialized_msg, football ):
    """Ingest extracted message.
    
    Parameters
    ----------
    serialized_msg : tarfile.ExFileObject
        Serialized raw object from tarfile.extractfile( message ).
    
    football : Cassandra football object
        The interface to Cassandra that gets passed around.
 
    Returns
    -------
    None
        Updates Cassandra through the football, then passes it.
    """
    CrayonMessage.from_msg( serialized_msg, football )

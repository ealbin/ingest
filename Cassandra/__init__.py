"""Cassandra interface

inteded use:
------------

    get_football()
        The football interfaces the back-end of 
        how and what to write to Cassandra across 
        tables across keyspaces.  Pass it around,
        and ask it to write for you.
        *note, once written to Cassandra, data is 
        purged from the football automatically.
        
        intended use:
            football = get_football()
            football.clear() # to reset at any time
            e.g.
                football.insert_run_config( basics ) 
                (run_config object is written to Cassandra,
                then cleared automatically)
"""

import Cassandra

def get_football():
    """Returns football.
    The football interfaces the back-end of 
    how and what to write to Cassandra across 
    tables across keyspaces.  Pass it around,
    and ask it to write for you.
    
    intended use:
        football = get_football()
        football.clear() # to reset at any time
        e.g.
            football.insert_run_config( basics ) 
    """
    return Cassandra.get_football()

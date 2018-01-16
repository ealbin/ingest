"""`misfits` Cassandra Football

Acts as the interface between Google protobuf
and Cassandra.  Updated by direct member access
as passed around.
"""

import format

class Football:

    def __init__(self):
        self.clear()
        
    def clear(self):
        self.errors       = None # varchar
        self.device_id    = None # varchar
        self.submit_time  = None # varint
        self.tarfile      = None # varchar
        self.tarmember    = None # varchar
        self.message      = None # blob

    def names(self):
        # must be same order as values()
        names = ''
        if self.errors      is not None: names += 'errors, '
        if self.device_id   is not None: names += 'device_id, '
        if self.submit_time is not None: names += 'submit_time, '
        if self.tarfile     is not None: names += 'tarfile, '
        if self.tarmember   is not None: names += 'tarmember, '
        if self.message     is not None: names += 'message, '
        if names != '': names = names[:-2]
        return names
            
    def values(self):
        # must be same order as names()
        values = ''
        if self.errors      is not None: values += format.varchar(self.errors)     + ', '
        if self.device_id   is not None: values += format.varchar(self.device_id)  + ', '
        if self.submit_time is not None: values += str(self.submit_time)           + ', '
        if self.tarfile     is not None: values += format.varchar(self.tarfile)    + ', ' 
        if self.tarmember   is not None: values += format.varchar(self.tarmemmber) + ', '
        if self.message     is not None: values += format.blob(self.message)       + ', '
        if values != '': values = values[:-2]
        return values

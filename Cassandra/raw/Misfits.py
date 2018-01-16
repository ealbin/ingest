import format

# misfits table

class Football:

    errors       = None # varchar
    device_id    = None # varchar
    submit_time  = None # varint
    tarfile      = None # varchar
    tarmember    = None # varchar
    message      = None # blob

    def clear(self):
        # should mirror above
        Football.errors       = None # varchar
        Football.device_id    = None # varchar
        Football.submit_time  = None # varint
        Football.tarfile      = None # varchar
        Football.tarmember    = None # varchar
        Football.message      = None # blob
        
    def names(self):
        # must be same order as values()
        names = ''
        print Football.device_id
        if Football.errors      is not None: names += 'errors, '
        if Football.device_id   is not None: names += 'device_id, '
        if Football.submit_time is not None: names += 'submit_time, '
        if Football.tarfile     is not None: names += 'tarfile, '
        if Football.tarmember   is not None: names += 'tarmember, '
        if Football.message     is not None: names += 'message'
        names.rstrip(', ')
        return names
            
    def values(self):
        # must be same order as names()
        values = ''
        if Football.errors      is not None: values += format.varchar(Football.errors)     + ', '
        if Football.device_id   is not None: values += format.varchar(Football.device_id)  + ', '
        if Football.submit_time is not None: values += str(Football.submit_time)           + ', '
        if Football.tarfile     is not None: values += format.varchar(Football.tarfile)    + ', ' 
        if Football.tarmember   is not None: values += format.varchar(Football.tarmemmber) + ', '
        if Football.message     is not None: values += format.blob(Football.message)       + ', '
        values.rstrip(', ')        
        return values

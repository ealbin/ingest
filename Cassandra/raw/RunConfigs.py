import format

# run_configs table

class Football:
    
    device_id     = None # varchar
    submit_time   = None # varint
    tarfile       = None # varchar
    tarmember     = None # varchar
    user_id       = None # varint
    app_code      = None # varchar
    remote_addr   = None # inet
    
    run_id        = None # varint
    run_id_hi     = None # varint
    
    start_time    = None # varint
    crayfis_build = None # varchar
    hw_params     = None # varchar
    os_params     = None # varchar
    camera_params = None # varchar
    camera_id     = None # varint

    def clear(self):
        # should mirror above
        Football.device_id     = None # varchar
        Football.submit_time   = None # varint
        Football.tarfile       = None # varchar
        Football.tarmember     = None # varchar
        Football.user_id       = None # varint
        Football.app_code      = None # varchar
        Football.remote_addr   = None # inet
        
        Football.run_id        = None # varint
        Football.run_id_hi     = None # varint
        
        Football.start_time    = None # varint
        Football.crayfis_build = None # varchar
        Football.hw_params     = None # varchar
        Football.os_params     = None # varchar
        Football.camera_params = None # varchar
        Football.camera_id     = None # varint
        
    def names(self):
        # must be in same order as values()
        names = ''
        if Football.device_id     is not None: names += 'device_id, '
        if Football.submit_time   is not None: names += 'submit_time, '
        if Football.tarfile       is not None: names += 'tarfile, '
        if Football.tarmember     is not None: names += 'tarmember, '        
        if Football.user_id       is not None: names += 'user_id, '
        if Football.app_code      is not None: names += 'app_code, '
        if Football.remote_addr   is not None: names += 'remote_addr, '
        if Football.run_id        is not None: names += 'run_id, '
        if Football.run_id_hi     is not None: names += 'run_id_hi, '
        if Football.start_time    is not None: names += 'start_time, '
        if Football.crayfis_build is not None: names += 'crayfis_build, '
        if Football.hw_params     is not None: names += 'hw_params, '
        if Football.os_params     is not None: names += 'os_params, '
        if Football.camera_params is not None: names += 'camera_params, '
        if Football.camera_id     is not None: names += 'camera_id, '
        names.rstrip(', ')
        return names               
    
    def values(self):
        # must be in same order as names()
        values = ''
        if Football.device_id     is not None: values += format.varchar(Football.device_id)     + ', '
        if Football.submit_time   is not None: values += str(Football.submit_time)              + ', '
        if Football.tarfile       is not None: values += format.varchar(Football.tarfile)       + ', '
        if Football.tarmember     is not None: values += format.varchar(Football.tarmember)     + ', '        
        if Football.user_id       is not None: values += str(Football.user_id)                  + ', '
        if Football.app_code      is not None: values += format.varchar(Football.app_code)      + ', '
        if Football.remote_addr   is not None: values += format.inet(Football.remote_addr)      + ', '
        if Football.run_id        is not None: values += str(Football.run_id)                   + ', '
        if Football.run_id_hi     is not None: values += str(Football.run_id_hi)                + ', '
        if Football.start_time    is not None: values += str(Football.start_time)               + ', '
        if Football.crayfis_build is not None: values += format.varchar(Football.crayfis_build) + ', '
        if Football.hw_params     is not None: values += format.varchar(Football.hw_params)     + ', '
        if Football.os_params     is not None: values += format.varchar(Football.os_params)     + ', '
        if Football.camera_params is not None: values += format.varchar(Football.camera_params) + ', '
        if Football.camera_id     is not None: values += str(Football.camera_id)                + ', '
        values.rstrip(', ')
        return values

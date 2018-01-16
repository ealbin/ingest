import format

# calibration_results table

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
    end_time      = None # varint
    
    hist_pixel    = None # set<varint>
    hist_l2pixel  = None # set<varint>
    hist_maxpixel = None # set<varint>
    hist_numpixel = None # set<varint>

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
        Football.end_time      = None # varint
        
        Football.hist_pixel    = None # set<varint>
        Football.hist_l2pixel  = None # set<varint>
        Football.hist_maxpixel = None # set<varint>
        Football.hist_numpixel = None # set<varint>        
            
    def names(self):
        # must be same order as values()
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
        if Football.end_time      is not None: names += 'end_time, '
        if Football.hist_pixel    is not None: names += 'hist_pixel, '
        if Football.hist_l2pixel  is not None: names += 'hist_l2pixel, '
        if Football.hist_maxpixel is not None: names += 'hist_maxpixel, '
        if Football.hist_numpixel is not None: names += 'hist_numpixel, '
        names.rstrip(', ')
        return names               
    
    def values(self):
        # must be same order as names()
        values = ''
        if Football.device_id     is not None: values += format.varchar(Football.device_id)        + ', '
        if Football.submit_time   is not None: values += str(Football.submit_time)                 + ', '
        if Football.tarfile       is not None: values += format.varchar(Football.tarfile)          + ', '
        if Football.tarmember     is not None: values += format.varchar(Football.tarmember)        + ', '        
        if Football.user_id       is not None: values += str(Football.user_id)                     + ', '
        if Football.app_code      is not None: values += format.varchar(Football.app_code)         + ', '
        if Football.remote_addr   is not None: values += format.inet(Football.remote_addr)         + ', '
        if Football.run_id        is not None: values += str(Football.run_id)                      + ', '
        if Football.run_id_hi     is not None: values += str(Football.run_id_hi)                   + ', '
        if Football.start_time    is not None: values += str(Football.start_time)                  + ', '
        if Football.end_time      is not None: values += str(Football.end_time)                    + ', '
        if Football.hist_pixel    is not None: values += format.set_varint(Football.hist_pixel)    + ', '
        if Football.hist_l2pixel  is not None: values += format.set_varint(Football.hist_l2pixel)  + ', '
        if Football.hist_maxpixel is not None: values += format.set_varint(Football.hist_maxpixel) + ', '
        if Football.hist_numpixel is not None: values += format.set_varint(Football.hist_numpixel) + ', '
        values.rstrip(', ')
        return values

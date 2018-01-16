import format

# precalibration_results table

class Football:
    
    device_id          = None # varchar
    submit_time        = None # varint
    tarfile            = None # varchar
    tarmember          = None # varchar
    user_id            = None # varint
    app_code           = None # varchar
    remote_addr        = None # inet
    
    run_id             = None # varint
    run_id_hi          = None # varint
    precal_id          = None # varint
    precal_id_hi       = None # varint
    
    start_time         = None # varint
    end_time           = None # varint
    
    weights            = None # set<double>
    
    sample_res_x       = None # varint
    sample_res_y       = None # varint
    interpolation      = None # varint
    battery_temp       = None # varint
    
    compressed_weights = None # varchar
    compressed_format  = None # varchar
    
    second_hist        = None # set<varint>
    hotcell            = None # set<varint>
    res_x              = None # varint

    def clear(self):
        # should mirror above
        Football.device_id          = None # varchar
        Football.submit_time        = None # varint
        Football.tarfile            = None # varchar
        Football.tarmember          = None # varchar
        Football.user_id            = None # varint
        Football.app_code           = None # varchar
        Football.remote_addr        = None # inet
        
        Football.run_id             = None # varint
        Football.run_id_hi          = None # varint
        Football.precal_id          = None # varint
        Football.precal_id_hi       = None # varint
        
        Football.start_time         = None # varint
        Football.end_time           = None # varint
        
        Football.weights            = None # set<double>
        
        Football.sample_res_x       = None # varint
        Football.sample_res_y       = None # varint
        Football.interpolation      = None # varint
        Football.battery_temp       = None # varint
        
        Football.compressed_weights = None # varchar
        Football.compressed_format  = None # varchar
        
        Football.second_hist        = None # set<varint>
        Football.hotcell            = None # set<varint>
        Football.res_x              = None # varint
        
    def names(self):
        # must be same order as values()
        names = ''
        if Football.device_id          is not None: names += 'device_id, '
        if Football.submit_time        is not None: names += 'submit_time, '
        if Football.tarfile            is not None: names += 'tarfile, '
        if Football.tarmember          is not None: names += 'tarmember, '        
        if Football.user_id            is not None: names += 'user_id, '
        if Football.app_code           is not None: names += 'app_code, '
        if Football.remote_addr        is not None: names += 'remote_addr, '
        if Football.run_id             is not None: names += 'run_id, '
        if Football.run_id_hi          is not None: names += 'run_id_hi, '
        if Football.precal_id          is not None: names += 'precal_id, '
        if Football.precal_id_hi       is not None: names += 'precal_id_hi, '
        if Football.start_time         is not None: names += 'start_time, '
        if Football.end_time           is not None: names += 'end_time, '
        if Football.weights            is not None: names += 'weights, '
        if Football.sample_res_x       is not None: names += 'sample_res_x, '
        if Football.sample_res_y       is not None: names += 'sample_res_y, '
        if Football.interpolation      is not None: names += 'interpolation, '
        if Football.battery_temp       is not None: names += 'battery_temp, '
        if Football.compressed_weights is not None: names += 'compress_weights, '        
        if Football.compressed_format  is not None: names += 'compress_format, '
        if Football.second_hist        is not None: names += 'second_hist, '
        if Football.hotcell            is not None: names += 'hotcell, '
        if Football.res_x              is not None: names += 'res_x, '
        names.rstrip(', ')
        return names               
    
    def values(self):
        # must be same order as names()
        values = ''
        if Football.device_id          is not None: values += format.varchar(Football.device_id)          + ', '
        if Football.submit_time        is not None: values += str(Football.submit_time)                   + ', '
        if Football.tarfile            is not None: values += format.varchar(Football.tarfile)            + ', '
        if Football.tarmember          is not None: values += format.varchar(Football.tarmember)          + ', '        
        if Football.user_id            is not None: values += str(Football.user_id)                       + ', '
        if Football.app_code           is not None: values += format.varchar(Football.app_code)           + ', '
        if Football.remote_addr        is not None: values += format.inet(Football.remote_addr)           + ', '
        if Football.run_id             is not None: values += str(Football.run_id)                        + ', '
        if Football.run_id_hi          is not None: values += str(Football.run_id_hi)                     + ', '
        if Football.precal_id          is not None: values += str(Football.precal_id)                     + ', '
        if Football.precal_id_hi       is not None: values += str(Football.precal_id_hi)                  + ', '
        if Football.start_time         is not None: values += str(Football.start_time)                    + ', '
        if Football.end_time           is not None: values += str(Football.end_time)                      + ', '
        if Football.weights            is not None: values += format.set_numeric(Football.weights)        + ', '
        if Football.sample_res_x       is not None: values += str(Football.sample_res_x)                  + ', '
        if Football.sample_res_y       is not None: values += str(Football.sample_res_y)                  + ', '
        if Football.interpolation      is not None: values += str(Football.interpolation)                 + ', '
        if Football.battery_temp       is not None: values += str(Football.battery_temp)                  + ', '
        if Football.compressed_weights is not None: values += format.varchar(Football.compressed_weights) + ', '
        if Football.compressed_format  is not None: values += format.varchar(Football.compressed_format)  + ', '
        if Football.second_hist        is not None: values += format.set_numeric(Football.second_hist)    + ', '
        if Football.hotcell            is not None: values += format.set_numeric(Football.hotcell)        + ', '
        if Football.res_x              is not None: values += str(Football.res_x)                         + ', '
        values.rstrip(', ')
        return values

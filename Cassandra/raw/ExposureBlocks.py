import format

# exposure_blocks table

class Football:
    device_id        = None # varchar
    submit_time      = None # varint
    tarfile          = None # varchar
    tarmember        = None # varchar
    user_id          = None # varint
    app_code         = None # varchar
    remote_addr      = None # inet
    
    precal_id        = None # varint
    precal_id_hi     = None # varint
    
    start_time       = None # varint
    end_time         = None # varint
    start_time_nano  = None # varint
    end_time_nano    = None # varint
    start_time_ntp   = None # varint
    end_time_ntp     = None # varint
    
    gps_lat          = None # double
    gps_lon          = None # double
    gps_altitude     = None # double
    gps_accuracy     = None # double
    gps_fixtime      = None # varint
    gps_fixtime_nano = None # varint
    
    battery_temp     = None # varint 
    battery_end_temp = None # varint 
    daq_state        = None # varchar 
    res_x            = None # varint
    res_y            = None # varint 
    
    L1_thresh        = None # varint 
    L2_thresh        = None # varint 
    L0_conf          = None # varchar
    L1_conf          = None # varchar
    L2_conf          = None # varchar
    L0_processed     = None # varint
    L1_processed     = None # varint
    L2_processed     = None # varint
    L0_pass          = None # varint
    L1_pass          = None # varint
    L2_pass          = None # varint
    L0_skip          = None # varint
    L1_skip          = None # varint
    L2_skip          = None # varint
    frames_dropped   = None # varint
    
    hist             = None # set<varint>
    xbn              = None #  varint
    aborted          = None # boolean
    
    event_ids        = None # set<uuid>

    def clear(self):
        # should mirror above
        device_id        = None # varchar
        Football.submit_time      = None # varint
        Football.tarfile          = None # varchar
        Football.tarmember        = None # varchar
        Football.user_id          = None # varint
        Football.app_code         = None # varchar
        Football.remote_addr      = None # inet
        
        Football.precal_id        = None # varint
        Football.precal_id_hi     = None # varint
        
        Football.start_time       = None # varint
        Football.end_time         = None # varint
        Football.start_time_nano  = None # varint
        Football.end_time_nano    = None # varint
        Football.start_time_ntp   = None # varint
        Football.end_time_ntp     = None # varint
        
        Football.gps_lat          = None # double
        Football.gps_lon          = None # double
        Football.gps_altitude     = None # double
        Football.gps_accuracy     = None # double
        Football.gps_fixtime      = None # varint
        Football.gps_fixtime_nano = None # varint
        
        Football.battery_temp     = None # varint 
        Football.battery_end_temp = None # varint 
        Football.daq_state        = None # varchar 
        Football.res_x            = None # varint
        Football.res_y            = None # varint 
        
        Football.L1_thresh        = None # varint 
        Football.L2_thresh        = None # varint 
        Football.L0_conf          = None # varchar
        Football.L1_conf          = None # varchar
        Football.L2_conf          = None # varchar
        Football.L0_processed     = None # varint
        Football.L1_processed     = None # varint
        Football.L2_processed     = None # varint
        Football.L0_pass          = None # varint
        Football.L1_pass          = None # varint
        Football.L2_pass          = None # varint
        Football.L0_skip          = None # varint
        Football.L1_skip          = None # varint
        Football.L2_skip          = None # varint
        Football.frames_dropped   = None # varint
        
        Football.hist             = None # set<varint>
        Football.xbn              = None # varint
        Football.aborted          = None # boolean
        
        Football.event_ids        = None # set<uuid>
    
        
    def names(self):
        # must be in same order as values()
        names = ''
        if Football.device_id        is not None: names += 'device_id, '
        if Football.submit_time      is not None: names += 'submit_time, '
        if Football.tarfile          is not None: names += 'tarfile, '
        if Football.tarmember        is not None: names += 'tarmember, '        
        if Football.user_id          is not None: names += 'user_id, '
        if Football.app_code         is not None: names += 'app_code, '
        if Football.remote_addr      is not None: names += 'remote_addr, '
        if Football.precal_id        is not None: names += 'precal_id, '
        if Football.precal_id_hi     is not None: names += 'precal_id_hi, '
        if Football.start_time       is not None: names += 'start_time, '
        if Football.end_time         is not None: names += 'end_time, '
        if Football.start_time_nano  is not None: names += 'start_time_nano, '
        if Football.end_time_nano    is not None: names += 'end_time_nano, '
        if Football.start_time_ntp   is not None: names += 'start_time_ntp, '
        if Football.end_time_ntp     is not None: names += 'end_time_ntp, '
        if Football.gps_lat          is not None: names += 'gps_lat, '
        if Football.gps_lon          is not None: names += 'gps_lon, '
        if Football.gps_altitude     is not None: names += 'gps_altitude, '
        if Football.gps_accuracy     is not None: names += 'gps_accuracy, '
        if Football.gps_fixtime      is not None: names += 'gps_fixtime, '
        if Football.gps_fixtime_nano is not None: names += 'gps_fixtime_nano, '
        if Football.battery_temp     is not None: names += 'battery_temp, '
        if Football.battery_end_temp is not None: names += 'battery_end_temp, '
        if Football.daq_state        is not None: names += 'daq_state, '
        if Football.res_x            is not None: names += 'res_x, '
        if Football.res_y            is not None: names += 'res_y, '
        if Football.L1_thresh        is not None: names += 'L1_thresh, '
        if Football.L2_thresh        is not None: names += 'L2_thresh, '
        if Football.L0_conf          is not None: names += 'L0_conf, '
        if Football.L1_conf          is not None: names += 'L1_conf, '
        if Football.L2_conf          is not None: names += 'L2_conf, '
        if Football.L0_processed     is not None: names += 'L0_processed, '
        if Football.L1_processed     is not None: names += 'L1_processed, '
        if Football.L2_processed     is not None: names += 'L2_processed, '
        if Football.L0_pass          is not None: names += 'L0_pass, '
        if Football.L1_pass          is not None: names += 'L1_pass, '
        if Football.L2_pass          is not None: names += 'L2_pass, '
        if Football.L0_skip          is not None: names += 'L0_skip, '
        if Football.L1_skip          is not None: names += 'L1_skip, '
        if Football.L2_skip          is not None: names += 'L2_skip, '
        if Football.frames_dropped   is not None: names += 'frames_dropped, '
        if Football.hist             is not None: names += 'hist, '
        if Football.xbn              is not None: names += 'xbn, '
        if Football.aborted          is not None: names += 'aborted, '
        if Football.event_ids        is not None: names += 'event_ids, '
        names.rstrip(', ')
        return names               
    
    def values(self):
        # must be in same order as names()
        values = ''
        if Football.device_id        is not None: values += format.varchar(Football.device_id)     + ', '
        if Football.submit_time      is not None: values += str(Football.submit_time)              + ', '
        if Football.tarfile          is not None: values += format.varchar(Football.tarfile)       + ', '
        if Football.tarmember        is not None: values += format.varchar(Football.tarmember)     + ', '        
        if Football.user_id          is not None: values += str(Football.user_id)                  + ', '
        if Football.app_code         is not None: values += format.varchar(Football.app_code)      + ', '
        if Football.remote_addr      is not None: values += format.inet(Football.remote_addr)      + ', '
        if Football.precal_id        is not None: values += str(Football.precal_id)                + ', '
        if Football.precal_id_hi     is not None: values += str(Football.precal_id_hi)             + ', '
        if Football.start_time       is not None: values += str(Football.start_time)               + ', '
        if Football.end_time         is not None: values += str(Football.end_time)                 + ', '
        if Football.start_time_nano  is not None: values += str(Football.start_time_nano)          + ', '
        if Football.end_time_nano    is not None: values += str(Football.end_time_nano)            + ', '
        if Football.start_time_ntp   is not None: values += str(Football.start_time_ntp)           + ', '
        if Football.end_time_ntp     is not None: values += str(Football.end_time_ntp)             + ', '
        if Football.gps_lat          is not None: values += str(Football.gps_lat)                  + ', '
        if Football.gps_lon          is not None: values += str(Football.gps_lon)                  + ', '
        if Football.gps_altitude     is not None: values += str(Football.gps_altitude)             + ', '
        if Football.gps_accuracy     is not None: values += str(Football.gps_accuracy)             + ', '
        if Football.gps_fixtime      is not None: values += str(Football.gps_fixtime)              + ', '        
        if Football.gps_fixtime_nano is not None: values += str(Football.gps_fixtime_nano)         + ', '
        if Football.battery_temp     is not None: values += str(Football.battery_temp)             + ', '
        if Football.battery_end_temp is not None: values += str(Football.battery_end_temp)         + ', '
        if Football.daq_state        is not None: values += format.varchar(Football.daq_state)     + ', '
        if Football.res_x            is not None: values += str(Football.res_x)                    + ', '
        if Football.res_y            is not None: values += str(Football.res_y)                    + ', '
        if Football.L1_thresh        is not None: values += str(Football.L1_thresh)                + ', '
        if Football.L2_thresh        is not None: values += str(Football.L2_thresh)                + ', '
        if Football.L0_conf          is not None: values += format.varchar(Football.L0_conf)       + ', '
        if Football.L1_conf          is not None: values += format.varchar(Football.L1_conf)       + ', '
        if Football.L2_conf          is not None: values += format.varchar(Football.L2_conf)       + ', '       
        if Football.L0_processed     is not None: values += str(Football.L0_processed)             + ', '
        if Football.L1_processed     is not None: values += str(Football.L1_processed)             + ', '
        if Football.L2_processed     is not None: values += str(Football.L2_processed)             + ', '
        if Football.L0_pass          is not None: values += str(Football.L0_pass)                  + ', '
        if Football.L1_pass          is not None: values += str(Football.L1_pass)                  + ', '
        if Football.L2_pass          is not None: values += str(Football.L2_pass)                  + ', '
        if Football.L0_skip          is not None: values += str(Football.L0_skip)                  + ', '
        if Football.L1_skip          is not None: values += str(Football.L1_skip)                  + ', '
        if Football.L2_skip          is not None: values += str(Football.L2_skip)                  + ', '
        if Football.frames_dropped   is not None: values += str(Football.frames_dropped)           + ', '
        if Football.hist             is not None: values += format.set_numeric(Football.hist)      + ', '
        if Football.xbn              is not None: values += str(Football.xbn)                      + ', '
        if Football.aborted          is not None: values += format.boolean(Football.aborted)       + ', '
        if Football.event_ids        is not None: values += format.set_numeric(Football.event_ids) + ', '
        values.rstrip(', ')
        return values

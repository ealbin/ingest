import format

# events table

class Football:
    device_id          = None # varchar
    submit_time        = None # varint
    tarfile            = None # varchar
    tarmember          = None # varchar
    user_id            = None # varint
    app_code           = None # varchar
    remote_addr        = None # inet

    event_id           = None # uuid
    run_id             = None # varint
    run_id_hi          = None # varint
    precal_id          = None # varint
    precal_id_hi       = None # varint
                        
    start_time         = None # varint
    end_time           = None # varint
    start_time_nano    = None # varint
    end_time_nano      = None # varint
    start_time_ntp     = None # varint
    end_time_ntp       = None # varint

    daq_state          = None # varchar 
    res_x              = None # varint
    res_y              = None # varint 
    
    L1_thresh          = None # varint 
    L2_thresh          = None # varint 
    L0_conf            = None # varchar
    L1_conf            = None # varchar
    L2_conf            = None # varchar
    L0_processed       = None # varint
    L1_processed       = None # varint
    L2_processed       = None # varint
    L0_pass            = None # varint
    L1_pass            = None # varint
    L2_pass            = None # varint
    L0_skip            = None # varint
    L1_skip            = None # varint
    L2_skip            = None # varint
    frames_dropped     = None # varint
    aborted            = None # boolean
        
    timestamp          = None # varint
    timestamp_nano     = None # varint
    timestamp_ntp      = None # varint
    timestamp_target   = None # varint
    
    gps_lat            = None # double
    gps_lon            = None # double
    gps_altitude       = None # double
    gps_accuracy       = None # double
    gps_fixtime        = None # varint
    gps_fixtime_nano   = None # varint
    
    battery_start_temp = None # varint 
    battery_temp       = None # varint
    battery_end_temp   = None # varint 
    pressure           = None # double
    orient_x           = None # double
    orient_y           = None # double
    orient_z           = None # double
                        
    avg                = None # double
    std                = None # double
    
    hist               = None # set<varint>
    xbn                = None # varint
    
    byte_block         = None # frozen <byteblock> 
    pixels             = None # set<frozen <pixel>>            
    zero_bias          = None # frozen <square>


    def clear(self):
        # should mirror above
        Football.device_id          = None # varchar
        Football.submit_time        = None # varint
        Football.tarfile            = None # varchar
        Football.tarmember          = None # varchar
        Football.user_id            = None # varint
        Football.app_code           = None # varchar
        Football.remote_addr        = None # inet
    
        Football.event_id           = None # uuid
        Football.run_id             = None # varint
        Football.run_id_hi          = None # varint
        Football.precal_id          = None # varint
        Football.precal_id_hi       = None # varint
                            
        Football.start_time         = None # varint
        Football.end_time           = None # varint
        Football.start_time_nano    = None # varint
        Football.end_time_nano      = None # varint
        Football.start_time_ntp     = None # varint
        Football.end_time_ntp       = None # varint
    
        Football.daq_state          = None # varchar 
        Football.res_x              = None # varint
        Football.res_y              = None # varint 
        
        Football.L1_thresh          = None # varint 
        Football.L2_thresh          = None # varint 
        Football.L0_conf            = None # varchar
        Football.L1_conf            = None # varchar
        Football.L2_conf            = None # varchar
        Football.L0_processed       = None # varint
        Football.L1_processed       = None # varint
        Football.L2_processed       = None # varint
        Football.L0_pass            = None # varint
        Football.L1_pass            = None # varint
        Football.L2_pass            = None # varint
        Football.L0_skip            = None # varint
        Football.L1_skip            = None # varint
        Football.L2_skip            = None # varint
        Football.frames_dropped     = None # varint
        Football.aborted            = None # boolean
            
        Football.timestamp          = None # varint
        Football.timestamp_nano     = None # varint
        Football.timestamp_ntp      = None # varint
        Football.timestamp_target   = None # varint
        
        Football.gps_lat            = None # double
        Football.gps_lon            = None # double
        Football.gps_altitude       = None # double
        Football.gps_accuracy       = None # double
        Football.gps_fixtime        = None # varint
        Football.gps_fixtime_nano   = None # varint
        
        Football.battery_start_temp = None # varint 
        Football.battery_temp       = None # varint
        Football.battery_end_temp   = None # varint 
        Football.pressure           = None # double
        Football.orient_x           = None # double
        Football.orient_y           = None # double
        Football.orient_z           = None # double
                            
        Football.avg                = None # double
        Football.std                = None # double
        
        Football.hist               = None # set<varint>
        Football.xbn                = None # varint
        
        Football.byte_block         = None # frozen <byteblock> 
        Football.pixels             = None # set<frozen <pixel>>            
        Football.zero_bias          = None # frozen <square>        
    
            
    def names(self):
        # must be in same order as values()
        names = ''
        if Football.device_id          is not None: names += 'device_id, '
        if Football.submit_time        is not None: names += 'submit_time, '
        if Football.tarfile            is not None: names += 'tarfile, '
        if Football.tarmember          is not None: names += 'tarmember, '        
        if Football.user_id            is not None: names += 'user_id, '
        if Football.app_code           is not None: names += 'app_code, '
        if Football.remote_addr        is not None: names += 'remote_addr, '
        if Football.event_id           is not None: names += 'event_id, '
        if Football.run_id             is not None: names += 'run_id, '
        if Football.run_id_hi          is not None: names += 'run_id_hi, '
        if Football.precal_id          is not None: names += 'precal_id, '
        if Football.precal_id_hi       is not None: names += 'precal_id_hi, '
        if Football.start_time         is not None: names += 'start_time, '
        if Football.end_time           is not None: names += 'end_time, '
        if Football.start_time_nano    is not None: names += 'start_time_nano, '
        if Football.end_time_nano      is not None: names += 'end_time_nano, '
        if Football.start_time_ntp     is not None: names += 'start_time_ntp, '
        if Football.end_time_ntp       is not None: names += 'end_time_ntp, '
        if Football.daq_state          is not None: names += 'daq_state, '
        if Football.res_x              is not None: names += 'res_x, '
        if Football.res_y              is not None: names += 'res_y, '
        if Football.L1_thresh          is not None: names += 'L1_thresh, '
        if Football.L2_thresh          is not None: names += 'L2_thresh, '
        if Football.L0_conf            is not None: names += 'L0_conf, '
        if Football.L1_conf            is not None: names += 'L1_conf, '
        if Football.L2_conf            is not None: names += 'L2_conf, '
        if Football.L0_processed       is not None: names += 'L0_processed, '
        if Football.L1_processed       is not None: names += 'L1_processed, '
        if Football.L2_processed       is not None: names += 'L2_processed, '
        if Football.L0_pass            is not None: names += 'L0_pass, '
        if Football.L1_pass            is not None: names += 'L1_pass, '
        if Football.L2_pass            is not None: names += 'L2_pass, '
        if Football.L0_skip            is not None: names += 'L0_skip, '
        if Football.L1_skip            is not None: names += 'L1_skip, '
        if Football.L2_skip            is not None: names += 'L2_skip, '
        if Football.frames_dropped     is not None: names += 'frames_dropped, '
        if Football.aborted            is not None: names += 'aborted, '
        if Football.timestamp          is not None: names += 'timestamp, '
        if Football.timestamp_nano     is not None: names += 'timestamp_nano, '
        if Football.timestamp_ntp      is not None: names += 'timestamp_ntp, '
        if Football.timestamp_target   is not None: names += 'timestamp_target, '        
        if Football.gps_lat            is not None: names += 'gps_lat, '
        if Football.gps_lon            is not None: names += 'gps_lon, '
        if Football.gps_altitude       is not None: names += 'gps_altitude, '
        if Football.gps_accuracy       is not None: names += 'gps_accuracy, '
        if Football.gps_fixtime        is not None: names += 'gps_fixtime, '
        if Football.gps_fixtime_nano   is not None: names += 'gps_fixtime_nano, '
        if Football.battery_start_temp is not None: names += 'battery_start_temp, '
        if Football.battery_temp       is not None: names += 'battery_temp, '
        if Football.battery_end_temp   is not None: names += 'battery_end_temp, '
        if Football.pressure           is not None: names += 'pressure, '
        if Football.orient_x           is not None: names += 'orient_x, '
        if Football.orient_y           is not None: names += 'orient_y, '
        if Football.orient_z           is not None: names += 'orient_z, '
        if Football.avg                is not None: names += 'avg, '
        if Football.std                is not None: names += 'std, '
        if Football.hist               is not None: names += 'hist, '
        if Football.xbn                is not None: names += 'xbn, '
        if Football.byte_block         is not None: names += 'byte_block, '
        if Football.pixels             is not None: names += 'pixels, '
        if Football.zero_bias          is not None: names += 'zero_bias, '
        names.rstrip(', ')
        return names               
    
    def values(self):
        # must be in same order as names()
        values = ''
        if Football.device_id          is not None: values += format.varchar(Football.device_id)     + ', '
        if Football.submit_time        is not None: values += str(Football.submit_time)              + ', '
        if Football.tarfile            is not None: values += format.varchar(Football.tarfile)       + ', '
        if Football.tarmember          is not None: values += format.varchar(Football.tarmember)     + ', '        
        if Football.user_id            is not None: values += str(Football.user_id)                  + ', '
        if Football.app_code           is not None: values += format.varchar(Football.app_code)      + ', '
        if Football.remote_addr        is not None: values += format.inet(Football.remote_addr)      + ', '
        if Football.event_id           is not None: values += str(Football.event_id)                 + ', '
        if Football.run_id             is not None: values += str(Football.run_id)                   + ', '
        if Football.run_id_hi          is not None: values += str(Football.run_id_hi)                + ', '
        if Football.precal_id          is not None: values += str(Football.precal_id)                + ', '
        if Football.precal_id_hi       is not None: values += str(Football.precal_id_hi)             + ', '
        if Football.start_time         is not None: values += str(Football.start_time)               + ', '
        if Football.end_time           is not None: values += str(Football.end_time)                 + ', '
        if Football.start_time_nano    is not None: values += str(Football.start_time_nano)          + ', '
        if Football.end_time_nano      is not None: values += str(Football.end_time_nano)            + ', '
        if Football.start_time_ntp     is not None: values += str(Football.start_time_ntp)           + ', '
        if Football.end_time_ntp       is not None: values += str(Football.end_time_ntp)             + ', '
        if Football.daq_state          is not None: values += format.varchar(Football.daq_state)     + ', '
        if Football.res_x              is not None: values += str(Football.res_x)                    + ', '
        if Football.res_y              is not None: values += str(Football.res_y)                    + ', '
        if Football.L1_thresh          is not None: values += str(Football.L1_thresh)                + ', '
        if Football.L2_thresh          is not None: values += str(Football.L2_thresh)                + ', '
        if Football.L0_conf            is not None: values += format.varchar(Football.L0_conf)       + ', '
        if Football.L1_conf            is not None: values += format.varchar(Football.L1_conf)       + ', '
        if Football.L2_conf            is not None: values += format.varchar(Football.L2_conf)       + ', '       
        if Football.L0_processed       is not None: values += str(Football.L0_processed)             + ', '
        if Football.L1_processed       is not None: values += str(Football.L1_processed)             + ', '
        if Football.L2_processed       is not None: values += str(Football.L2_processed)             + ', '
        if Football.L0_pass            is not None: values += str(Football.L0_pass)                  + ', '
        if Football.L1_pass            is not None: values += str(Football.L1_pass)                  + ', '
        if Football.L2_pass            is not None: values += str(Football.L2_pass)                  + ', '
        if Football.L0_skip            is not None: values += str(Football.L0_skip)                  + ', '
        if Football.L1_skip            is not None: values += str(Football.L1_skip)                  + ', '
        if Football.L2_skip            is not None: values += str(Football.L2_skip)                  + ', '
        if Football.frames_dropped     is not None: values += str(Football.frames_dropped)           + ', '
        if Football.aborted            is not None: values += format.boolean(Football.aborted)       + ', '
        if Football.timestamp          is not None: values += str(Football.timestamp)                + ', '
        if Football.timestamp_nano     is not None: values += str(Football.timestamp_nano)           + ', '
        if Football.timestamp_ntp      is not None: values += str(Football.timestamp_ntp)            + ', '
        if Football.timestamp_target   is not None: values += str(Football.timestamp_target)         + ', '
        if Football.gps_lat            is not None: values += str(Football.gps_lat)                  + ', '
        if Football.gps_lon            is not None: values += str(Football.gps_lon)                  + ', '
        if Football.gps_altitude       is not None: values += str(Football.gps_altitude)             + ', '
        if Football.gps_accuracy       is not None: values += str(Football.gps_accuracy)             + ', '
        if Football.gps_fixtime        is not None: values += str(Football.gps_fixtime)              + ', '        
        if Football.gps_fixtime_nano   is not None: values += str(Football.gps_fixtime_nano)         + ', '
        if Football.battery_start_temp is not None: values += str(Football.battery_start_temp)       + ', '
        if Football.battery_temp       is not None: values += str(Football.battery_temp)             + ', '
        if Football.battery_end_temp   is not None: values += str(Football.battery_end_temp)         + ', '
        if Football.pressure           is not None: values += str(Football.pressure)                 + ', '
        if Football.orient_x           is not None: values += str(Football.orient_x)                 + ', '
        if Football.orient_y           is not None: values += str(Football.orient_y)                 + ', '
        if Football.orient_z           is not None: values += str(Football.orient_z)                 + ', '
        if Football.avg                is not None: values += str(Football.avg)                      + ', '
        if Football.std                is not None: values += str(Football.std)                      + ', '
        if Football.hist               is not None: values += format.set_numeric(Football.hist)      + ', '
        if Football.xbn                is not None: values += str(Football.xbn)                      + ', '
        if Football.byte_block         is not None: values += format.byte_block(Football.byte_block) + ', '
        if Football.pixels             is not None: values += format.pixels(Football.pixels)         + ', '
        if Football.zero_bias          is not None: values += format.zero_bias(Football.zer_bias)    + ', '
        values.rstrip(', ')
        return values

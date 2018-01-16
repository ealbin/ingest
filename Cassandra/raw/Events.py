"""`events` Cassandra Football

Acts as the interface between Google protobuf
and Cassandra.  Updated by direct member access
as passed around.
"""

import format

class Football:

    def __init__(self):
        self.clear()

    def clear(self):
        self.device_id          = None # varchar
        self.submit_time        = None # varint
        self.tarfile            = None # varchar
        self.tarmember          = None # varchar
        self.user_id            = None # varint
        self.app_code           = None # varchar
        self.remote_addr        = None # inet
    
        self.event_id           = None # uuid
        self.run_id             = None # varint
        self.run_id_hi          = None # varint
        self.precal_id          = None # varint
        self.precal_id_hi       = None # varint
                            
        self.start_time         = None # varint
        self.end_time           = None # varint
        self.start_time_nano    = None # varint
        self.end_time_nano      = None # varint
        self.start_time_ntp     = None # varint
        self.end_time_ntp       = None # varint
    
        self.daq_state          = None # varchar 
        self.res_x              = None # varint
        self.res_y              = None # varint 
        
        self.L1_thresh          = None # varint 
        self.L2_thresh          = None # varint 
        self.L0_conf            = None # varchar
        self.L1_conf            = None # varchar
        self.L2_conf            = None # varchar
        self.L0_processed       = None # varint
        self.L1_processed       = None # varint
        self.L2_processed       = None # varint
        self.L0_pass            = None # varint
        self.L1_pass            = None # varint
        self.L2_pass            = None # varint
        self.L0_skip            = None # varint
        self.L1_skip            = None # varint
        self.L2_skip            = None # varint
        self.frames_dropped     = None # varint
        self.aborted            = None # boolean
            
        self.timestamp          = None # varint
        self.timestamp_nano     = None # varint
        self.timestamp_ntp      = None # varint
        self.timestamp_target   = None # varint
        
        self.gps_lat            = None # double
        self.gps_lon            = None # double
        self.gps_altitude       = None # double
        self.gps_accuracy       = None # double
        self.gps_fixtime        = None # varint
        self.gps_fixtime_nano   = None # varint
        
        self.battery_start_temp = None # varint 
        self.battery_temp       = None # varint
        self.battery_end_temp   = None # varint 
        self.pressure           = None # double
        self.orient_x           = None # double
        self.orient_y           = None # double
        self.orient_z           = None # double
                            
        self.avg                = None # double
        self.std                = None # double
        
        self.hist               = None # set<varint>
        self.xbn                = None # varint
        
        self.byte_block         = None # frozen <byteblock> 
        self.pixels             = None # set<frozen <pixel>>            
        self.zero_bias          = None # frozen <square>        
    
            
    def names(self):
        # must be in same order as values()
        names = ''
        if self.device_id          is not None: names += 'device_id, '
        if self.submit_time        is not None: names += 'submit_time, '
        if self.tarfile            is not None: names += 'tarfile, '
        if self.tarmember          is not None: names += 'tarmember, '        
        if self.user_id            is not None: names += 'user_id, '
        if self.app_code           is not None: names += 'app_code, '
        if self.remote_addr        is not None: names += 'remote_addr, '
        if self.event_id           is not None: names += 'event_id, '
        if self.run_id             is not None: names += 'run_id, '
        if self.run_id_hi          is not None: names += 'run_id_hi, '
        if self.precal_id          is not None: names += 'precal_id, '
        if self.precal_id_hi       is not None: names += 'precal_id_hi, '
        if self.start_time         is not None: names += 'start_time, '
        if self.end_time           is not None: names += 'end_time, '
        if self.start_time_nano    is not None: names += 'start_time_nano, '
        if self.end_time_nano      is not None: names += 'end_time_nano, '
        if self.start_time_ntp     is not None: names += 'start_time_ntp, '
        if self.end_time_ntp       is not None: names += 'end_time_ntp, '
        if self.daq_state          is not None: names += 'daq_state, '
        if self.res_x              is not None: names += 'res_x, '
        if self.res_y              is not None: names += 'res_y, '
        if self.L1_thresh          is not None: names += 'L1_thresh, '
        if self.L2_thresh          is not None: names += 'L2_thresh, '
        if self.L0_conf            is not None: names += 'L0_conf, '
        if self.L1_conf            is not None: names += 'L1_conf, '
        if self.L2_conf            is not None: names += 'L2_conf, '
        if self.L0_processed       is not None: names += 'L0_processed, '
        if self.L1_processed       is not None: names += 'L1_processed, '
        if self.L2_processed       is not None: names += 'L2_processed, '
        if self.L0_pass            is not None: names += 'L0_pass, '
        if self.L1_pass            is not None: names += 'L1_pass, '
        if self.L2_pass            is not None: names += 'L2_pass, '
        if self.L0_skip            is not None: names += 'L0_skip, '
        if self.L1_skip            is not None: names += 'L1_skip, '
        if self.L2_skip            is not None: names += 'L2_skip, '
        if self.frames_dropped     is not None: names += 'frames_dropped, '
        if self.aborted            is not None: names += 'aborted, '
        if self.timestamp          is not None: names += 'timestamp, '
        if self.timestamp_nano     is not None: names += 'timestamp_nano, '
        if self.timestamp_ntp      is not None: names += 'timestamp_ntp, '
        if self.timestamp_target   is not None: names += 'timestamp_target, '        
        if self.gps_lat            is not None: names += 'gps_lat, '
        if self.gps_lon            is not None: names += 'gps_lon, '
        if self.gps_altitude       is not None: names += 'gps_altitude, '
        if self.gps_accuracy       is not None: names += 'gps_accuracy, '
        if self.gps_fixtime        is not None: names += 'gps_fixtime, '
        if self.gps_fixtime_nano   is not None: names += 'gps_fixtime_nano, '
        if self.battery_start_temp is not None: names += 'battery_start_temp, '
        if self.battery_temp       is not None: names += 'battery_temp, '
        if self.battery_end_temp   is not None: names += 'battery_end_temp, '
        if self.pressure           is not None: names += 'pressure, '
        if self.orient_x           is not None: names += 'orient_x, '
        if self.orient_y           is not None: names += 'orient_y, '
        if self.orient_z           is not None: names += 'orient_z, '
        if self.avg                is not None: names += 'avg, '
        if self.std                is not None: names += 'std, '
        if self.hist               is not None: names += 'hist, '
        if self.xbn                is not None: names += 'xbn, '
        if self.byte_block         is not None: names += 'byte_block, '
        if self.pixels             is not None: names += 'pixels, '
        if self.zero_bias          is not None: names += 'zero_bias, '
        if names != '': names = names[:-2]
        return names               
    
    def values(self):
        # must be in same order as names()
        values = ''
        if self.device_id          is not None: values += format.varchar(self.device_id)     + ', '
        if self.submit_time        is not None: values += str(self.submit_time)              + ', '
        if self.tarfile            is not None: values += format.varchar(self.tarfile)       + ', '
        if self.tarmember          is not None: values += format.varchar(self.tarmember)     + ', '        
        if self.user_id            is not None: values += str(self.user_id)                  + ', '
        if self.app_code           is not None: values += format.varchar(self.app_code)      + ', '
        if self.remote_addr        is not None: values += format.inet(self.remote_addr)      + ', '
        if self.event_id           is not None: values += str(self.event_id)                 + ', '
        if self.run_id             is not None: values += str(self.run_id)                   + ', '
        if self.run_id_hi          is not None: values += str(self.run_id_hi)                + ', '
        if self.precal_id          is not None: values += str(self.precal_id)                + ', '
        if self.precal_id_hi       is not None: values += str(self.precal_id_hi)             + ', '
        if self.start_time         is not None: values += str(self.start_time)               + ', '
        if self.end_time           is not None: values += str(self.end_time)                 + ', '
        if self.start_time_nano    is not None: values += str(self.start_time_nano)          + ', '
        if self.end_time_nano      is not None: values += str(self.end_time_nano)            + ', '
        if self.start_time_ntp     is not None: values += str(self.start_time_ntp)           + ', '
        if self.end_time_ntp       is not None: values += str(self.end_time_ntp)             + ', '
        if self.daq_state          is not None: values += format.varchar(self.daq_state)     + ', '
        if self.res_x              is not None: values += str(self.res_x)                    + ', '
        if self.res_y              is not None: values += str(self.res_y)                    + ', '
        if self.L1_thresh          is not None: values += str(self.L1_thresh)                + ', '
        if self.L2_thresh          is not None: values += str(self.L2_thresh)                + ', '
        if self.L0_conf            is not None: values += format.varchar(self.L0_conf)       + ', '
        if self.L1_conf            is not None: values += format.varchar(self.L1_conf)       + ', '
        if self.L2_conf            is not None: values += format.varchar(self.L2_conf)       + ', '       
        if self.L0_processed       is not None: values += str(self.L0_processed)             + ', '
        if self.L1_processed       is not None: values += str(self.L1_processed)             + ', '
        if self.L2_processed       is not None: values += str(self.L2_processed)             + ', '
        if self.L0_pass            is not None: values += str(self.L0_pass)                  + ', '
        if self.L1_pass            is not None: values += str(self.L1_pass)                  + ', '
        if self.L2_pass            is not None: values += str(self.L2_pass)                  + ', '
        if self.L0_skip            is not None: values += str(self.L0_skip)                  + ', '
        if self.L1_skip            is not None: values += str(self.L1_skip)                  + ', '
        if self.L2_skip            is not None: values += str(self.L2_skip)                  + ', '
        if self.frames_dropped     is not None: values += str(self.frames_dropped)           + ', '
        if self.aborted            is not None: values += format.boolean(self.aborted)       + ', '
        if self.timestamp          is not None: values += str(self.timestamp)                + ', '
        if self.timestamp_nano     is not None: values += str(self.timestamp_nano)           + ', '
        if self.timestamp_ntp      is not None: values += str(self.timestamp_ntp)            + ', '
        if self.timestamp_target   is not None: values += str(self.timestamp_target)         + ', '
        if self.gps_lat            is not None: values += str(self.gps_lat)                  + ', '
        if self.gps_lon            is not None: values += str(self.gps_lon)                  + ', '
        if self.gps_altitude       is not None: values += str(self.gps_altitude)             + ', '
        if self.gps_accuracy       is not None: values += str(self.gps_accuracy)             + ', '
        if self.gps_fixtime        is not None: values += str(self.gps_fixtime)              + ', '        
        if self.gps_fixtime_nano   is not None: values += str(self.gps_fixtime_nano)         + ', '
        if self.battery_start_temp is not None: values += str(self.battery_start_temp)       + ', '
        if self.battery_temp       is not None: values += str(self.battery_temp)             + ', '
        if self.battery_end_temp   is not None: values += str(self.battery_end_temp)         + ', '
        if self.pressure           is not None: values += str(self.pressure)                 + ', '
        if self.orient_x           is not None: values += str(self.orient_x)                 + ', '
        if self.orient_y           is not None: values += str(self.orient_y)                 + ', '
        if self.orient_z           is not None: values += str(self.orient_z)                 + ', '
        if self.avg                is not None: values += str(self.avg)                      + ', '
        if self.std                is not None: values += str(self.std)                      + ', '
        if self.hist               is not None: values += format.set_numeric(self.hist)      + ', '
        if self.xbn                is not None: values += str(self.xbn)                      + ', '
        if self.byte_block         is not None: values += format.byte_block(self.byte_block) + ', '
        if self.pixels             is not None: values += format.pixels(self.pixels)         + ', '
        if self.zero_bias          is not None: values += format.zero_bias(self.zer_bias)    + ', '
        if values != '': values = values[:-2]
        return values

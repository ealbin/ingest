"""`precalibration_results` Cassandra Football

Acts as the interface between Google protobuf
and Cassandra.  Updated by set_() functions.
Cassandra-compatable strings are returned by
get_() functions.

"""

import writer.format as format

class Football:
    
    def __init__(self):
        self.__debug_mode = False
        self.clear()

    def clear(self):
        self.device_id          = None # varchar
        self.submit_time        = None # varint
        self.tarfile            = None # varchar
        self.tarmember          = None # varchar
        self.host               = None # varchar
        self.user_id            = None # varint
        self.app_code           = None # varchar
        self.remote_addr        = None # inet
        
        self.run_id             = None # varint
        self.run_id_hi          = None # varint
        self.precal_id          = None # varint
        self.precal_id_hi       = None # varint
        
        self.start_time         = None # varint
        self.end_time           = None # varint
        
        self.weights            = None # set<double>
        
        self.sample_res_x       = None # varint
        self.sample_res_y       = None # varint
        self.interpolation      = None # varint
        self.battery_temp       = None # varint
        
        self.compressed_weights = None # varchar
        self.compressed_format  = None # varchar
        
        self.second_hist        = None # set<varint>
        self.hotcell            = None # set<varint>
        self.res_x              = None # varint
        if self.__debug_mode: print '[raw.precalibration_result] cleared'
        
    def get_names(self):
        # must be same order as get_values()
        names = ''
        if self.device_id          is not None: names += 'device_id, '
        if self.submit_time        is not None: names += 'submit_time, '
        if self.tarfile            is not None: names += 'tarfile, '
        if self.tarmember          is not None: names += 'tarmember, '        
        if self.host               is not None: names += 'host, '
        if self.user_id            is not None: names += 'user_id, '
        if self.app_code           is not None: names += 'app_code, '
        if self.remote_addr        is not None: names += 'remote_addr, '
        if self.run_id             is not None: names += 'run_id, '
        if self.run_id_hi          is not None: names += 'run_id_hi, '
        if self.precal_id          is not None: names += 'precal_id, '
        if self.precal_id_hi       is not None: names += 'precal_id_hi, '
        if self.start_time         is not None: names += 'start_time, '
        if self.end_time           is not None: names += 'end_time, '
        if self.weights            is not None: names += 'weights, '
        if self.sample_res_x       is not None: names += 'sample_res_x, '
        if self.sample_res_y       is not None: names += 'sample_res_y, '
        if self.interpolation      is not None: names += 'interpolation, '
        if self.battery_temp       is not None: names += 'battery_temp, '
        if self.compressed_weights is not None: names += 'compress_weights, '        
        if self.compressed_format  is not None: names += 'compress_format, '
        if self.second_hist        is not None: names += 'second_hist, '
        if self.hotcell            is not None: names += 'hotcell, '
        if self.res_x              is not None: names += 'res_x, '
        if names != '': names = names[:-2]
        if self.__debug_mode: print '[raw.precalibration_result] names: ' + names
        return names               
    
    def get_values(self):
        # must be same order as get_names()
        values = ''
        if self.device_id          is not None: values += format.varchar(self.device_id)          + ', '
        if self.submit_time        is not None: values += str(self.submit_time)                   + ', '
        if self.tarfile            is not None: values += format.varchar(self.tarfile)            + ', '
        if self.tarmember          is not None: values += format.varchar(self.tarmember)          + ', '        
        if self.host               is not None: values += format.varchar(self.host)               + ', '
        if self.user_id            is not None: values += str(self.user_id)                       + ', '
        if self.app_code           is not None: values += format.varchar(self.app_code)           + ', '
        if self.remote_addr        is not None: values += format.inet(self.remote_addr)           + ', '
        if self.run_id             is not None: values += str(self.run_id)                        + ', '
        if self.run_id_hi          is not None: values += str(self.run_id_hi)                     + ', '
        if self.precal_id          is not None: values += str(self.precal_id)                     + ', '
        if self.precal_id_hi       is not None: values += str(self.precal_id_hi)                  + ', '
        if self.start_time         is not None: values += str(self.start_time)                    + ', '
        if self.end_time           is not None: values += str(self.end_time)                      + ', '
        if self.weights            is not None: values += format.set_numeric(self.weights)        + ', '
        if self.sample_res_x       is not None: values += str(self.sample_res_x)                  + ', '
        if self.sample_res_y       is not None: values += str(self.sample_res_y)                  + ', '
        if self.interpolation      is not None: values += str(self.interpolation)                 + ', '
        if self.battery_temp       is not None: values += str(self.battery_temp)                  + ', '
        if self.compressed_weights is not None: values += format.varchar(self.compressed_weights) + ', '
        if self.compressed_format  is not None: values += format.varchar(self.compressed_format)  + ', '
        if self.second_hist        is not None: values += format.set_numeric(self.second_hist)    + ', '
        if self.hotcell            is not None: values += format.set_numeric(self.hotcell)        + ', '
        if self.res_x              is not None: values += str(self.res_x)                         + ', '
        if values != '': values = values[:-2]
        if self.__debug_mode: print '[raw.precalibration_result] values[:100]: ' + values[:100]
        return values

    def set_metadata(self, host='', tarfile='', tarmember=''):
        self.host      = host
        self.tarfile   = tarfile
        self.tarmember = tarmember
        if self.__debug_mode: print '[raw.precalibration_result] metadata set'
        return True

    def set_basics(self, basics ):
        for basic in basics:
            try:
                setattr( self, basic['field'].name, basic['value'] )
            except Exception as e:
                if self.__debug_mode: print '[raw.precalibration_result] attribute unknown: ' + basic['field'].name
                return False
        if self.__debug_mode: print '[raw.precalibration_result] basics set'
        return True


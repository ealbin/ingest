"""`run_configs` Cassandra Football

Acts as the interface between Google protobuf
and Cassandra.  Updated by set_() functions.
Cassandra-compatable strings are returned by
get_() functions.

"""

import format

class Football:

    def __init__(self):
        self.__debug_mode = False
        self.clear()

    def clear(self):
        self.device_id     = None # varchar
        self.submit_time   = None # varint
        self.tarfile       = None # varchar
        self.tarmember     = None # varchar
        self.host          = None # varchar
        self.user_id       = None # varint
        self.app_code      = None # varchar
        self.remote_addr   = None # inet
        
        # appears as id / id_hi in Google protobuf
        # appears as run_id / run_id_hi in Cassandra
        self.id            = None # varint
        self.id_hi         = None # varint
        
        self.start_time    = None # varint
        self.crayfis_build = None # varchar
        self.hw_params     = None # varchar
        self.os_params     = None # varchar
        self.camera_params = None # varchar
        self.camera_id     = None # varint
        if self.__debug_mode: print '[raw.run_config] cleared'
        
    def get_names(self):
        # must be in same order as get_values()
        names = ''
        if self.device_id     is not None: names += 'device_id, '
        if self.submit_time   is not None: names += 'submit_time, '
        if self.tarfile       is not None: names += 'tarfile, '
        if self.tarmember     is not None: names += 'tarmember, '        
        if self.host          is not None: names += 'host, '
        if self.user_id       is not None: names += 'user_id, '
        if self.app_code      is not None: names += 'app_code, '
        if self.remote_addr   is not None: names += 'remote_addr, '
        if self.id            is not None: names += 'run_id, '
        if self.id_hi         is not None: names += 'run_id_hi, '
        if self.start_time    is not None: names += 'start_time, '
        if self.crayfis_build is not None: names += 'crayfis_build, '
        if self.hw_params     is not None: names += 'hw_params, '
        if self.os_params     is not None: names += 'os_params, '
        if self.camera_params is not None: names += 'camera_params, '
        if self.camera_id     is not None: names += 'camera_id, '
        if names != '': names = names[:-2]
        if self.__debug_mode: print '[raw.run_config] names: ' + names
        return names               
    
    def get_values(self):
        # must be in same order as get_names()
        values = ''
        if self.device_id     is not None: values += format.varchar(self.device_id)     + ', '
        if self.submit_time   is not None: values += str(self.submit_time)              + ', '
        if self.tarfile       is not None: values += format.varchar(self.tarfile)       + ', '
        if self.tarmember     is not None: values += format.varchar(self.tarmember)     + ', '        
        if self.host          is not None: values += format.varchar(self.host)          + ', '
        if self.user_id       is not None: values += str(self.user_id)                  + ', '
        if self.app_code      is not None: values += format.varchar(self.app_code)      + ', '
        if self.remote_addr   is not None: values += format.inet(self.remote_addr)      + ', '
        if self.id            is not None: values += str(self.id)                       + ', '
        if self.id_hi         is not None: values += str(self.id_hi)                    + ', '
        if self.start_time    is not None: values += str(self.start_time)               + ', '
        if self.crayfis_build is not None: values += format.varchar(self.crayfis_build) + ', '
        if self.hw_params     is not None: values += format.varchar(self.hw_params)     + ', '
        if self.os_params     is not None: values += format.varchar(self.os_params)     + ', '
        if self.camera_params is not None: values += format.varchar(self.camera_params) + ', '
        if self.camera_id     is not None: values += str(self.camera_id)                + ', '
        if values != '': values = values[:-2]
        if self.__debug_mode: print '[raw.run_config] values[:100]: ' + values[:100]
        return values

    def set_metadata(self, host='', tarfile='', tarmember=''):
        self.host      = host
        self.tarfile   = tarfile
        self.tarmember = tarmember
        if self.__debug_mode: print '[raw.run_config] metadata set'
        return True

    def set_basics(self, basics ):
        for basic in basics:
            try:
                setattr( self, basic['field'].name, basic['value'] )
            except Exception as e:
                if self.__debug_mode: print '[raw.run_config] attribute unknown: ' + basic['field'].name
                return False
        if self.__debug_mode: print '[raw.run_config] basics set'
        return True


"""`misfits` Cassandra Football

Acts as the interface between Google protobuf
and Cassandra.  Updated by set_() functions.
Cassandra-compatable strings are returned by
get_() functions.

"""

from ..writer import compose as compose

class Football:

    def __init__(self):
        self.__debug_mode = False
        self.clear()
        
    def add_error(self, error_string):
        if self.errors is not None:
            self.errors += '; ' + error_string
        else:
            self.errors = error_string
        if self.__debug_mode: print '[raw.misfit] error added: "' + error_string + '"'

    def clear(self):
        self.errors       = None # varchar
        self.device_id    = None # varchar
        self.submit_time  = None # varint
        self.tarfile      = None # varchar
        self.tarmember    = None # varchar
        self.host         = None # varchar
        self.message      = None # blob
        if self.__debug_mode: print '[raw.misfit] cleared'

    def get_names(self):
        # must be same order as get_values()
        names = ''
        if self.errors      is not None: names += 'errors, '
        if self.device_id   is not None: names += 'device_id, '
        if self.submit_time is not None: names += 'submit_time, '
        if self.tarfile     is not None: names += 'tarfile, '
        if self.tarmember   is not None: names += 'tarmember, '
        if self.host        is not None: names += 'host, '
        if self.message     is not None: names += 'message, '
        if names != '': names = names[:-2]
        if self.__debug_mode: print '[raw.misfit] names: ' + names
        return names
            
    def get_values(self):
        # must be same order as get_names()
        values = ''
        if self.errors      is not None: values += compose.varchar(self.errors)     + ', '
        if self.device_id   is not None: values += compose.varchar(self.device_id)  + ', '
        if self.submit_time is not None: values += str(self.submit_time)           + ', '
        if self.tarfile     is not None: values += compose.varchar(self.tarfile)    + ', ' 
        if self.tarmember   is not None: values += compose.varchar(self.tarmember)  + ', '
        if self.host        is not None: values += compose.varchar(self.host)       + ', '
        if self.message     is not None: values += compose.blob(self.message)       + ', '
        if values != '': values = values[:-2]
        if self.__debug_mode: print '[raw.misfit] values[:100]: ' + values[:100]
        return values

    def set_metadata(self, host='', tarfile='', tarmember=''):
        self.host      = host
        self.tarfile   = tarfile
        self.tarmember = tarmember
        if self.__debug_mode: print '[raw.misfit] metadata set'
        return True
    
    def set_serialized(self, serialized_string):
        self.message = serialized_string
        if self.__debug_mode: print '[raw.misfit] serialized message[:100]: ' + repr(serialized_string)[1:101]
        return True

    def set_attributes(self, basics ):
        for basic in basics:
            try:
                setattr( self, basic['field'].name, basic['value'] )
            except Exception as e:
                print '[raw.misfit] attribute unknown: ' + basic['field'].name
                return False
        if self.__debug_mode: print '[raw.misfit] basics set'
        return True

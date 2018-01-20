




def insert( table, names='', values='' ):
    print
    print '     INSERT into ' + table + ' ( ' + names + ' )'
    print '     VALUES ( ' + values[:70] + ' ... ' + values[-70:] + ' )'
    print


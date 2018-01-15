

import time
import os 
import ingest

origin = '/mnt/c/Users/EricK/crayfis/cassandra-dev/craydata/' #'/data/daq.crayfis.io/raw/2018/'  # data source
print 'tarfile source: ' + origin

tarfiles = []
for path, directories, files in os.walk( origin ):
    if '_old/' in path: continue

    for filename in files:
        if filename.endswith('.tar.gz'):
            tarfiles.append( os.path.join(path,filename) )
tarfiles = sorted( tarfiles, key=lambda k: k.lower(), reverse=True )
print 'messages found: {}'.format(len(tarfiles))
print

start = time.time()
for file_n, file in enumerate(tarfiles):
    ingest.from_tarfile( file )
    print
#    print 'Progress: file {0} of {1}, msg fails: {2}, successes: {3}, seconds: {4}\r'.format( file_n+1, len(tarfiles), fails, successes, time.time() - start ),
        
print 'seconds: {0}'.format( time.time() - start )
print 'done.'



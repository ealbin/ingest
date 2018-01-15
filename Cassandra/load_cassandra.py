# todo:  include tarfile and member in header
# todo:  make reject/misfits database with "reason" column (text)
# todo:  push into payload and complete error check / write to expo/run/cal keyspaces

import init_cassandra
from write_cassandra import write_message

import time
import os      as os
import tarfile as tarf

origin = '/data/daq.crayfis.io/raw'  # data source
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

fails = 0
successes = 0
start = time.time()
for file_n, file in enumerate(tarfiles):
    tarfile = tarf.open( file, 'r:gz' )
    messages = [ member for member in tarfile.getmembers() if member.name.endswith('.msg') ]

    for message in messages:
        metadata = [ {'name':'tarfile', 'value':file}, {'name':'message', 'value':message.name} ]
        msg = tarfile.extractfile( message, metadata )
        success = write_message( msg )
        if not success:
            fails += 1
        else:
            successes += 1

        print 'Progress: file {0} of {1}, msg fails: {2}, successes: {3}, seconds: {4}\r'.format( file_n+1, len(tarfiles), fails, successes, time.time() - start ),
        
    tarfile.close()
print 'Progress: file {0} of {1}, msg fails: {2}, successes: {3}, seconds: {4}'.format( file_n+1, len(tarfiles), fails, successes, time.time() - start )
print 'done.'


from crayvault import get_session
import sys

__session = get_session()

#-----------------------------------------------------------------------------
# KEYSPACE: raw

def clear():
    progress = [ '|', '\\', '--', '/' ]
    i = 0
    print '>> WARNING clearing Cassandra, starting fresh...'
    while (True):
        try:
            __session.execute( 'DROP KEYSPACE IF EXISTS raw' ) #!! clean start
        except Exception as e:
            print '\r>> waiting on Cassandra...{0}'.format(progress[i % 4]),
            sys.stdout.flush()
            i += 1
            continue
        print '\r>> waiting on Cassandra... done.'
        sys.stdout.flush()
        break

#-----------------------------------------------------------------------------

def do_it():
    __session.execute( """CREATE KEYSPACE IF NOT EXISTS raw
                        WITH replication = {'class':'SimpleStrategy','replication_factor':1};""" )
    
    
    # type definitions
    #------------------
    
    # pixel type def
    __session.execute( """CREATE TYPE IF NOT EXISTS raw.pixel (
                        x               varint,
                        y               varint,
                        val             varint,
                        adjusted_val    varint,
                        near_max        varint,
                        ave_3           double,
                        ave_5           double );""" )
    
    # square type def
    __session.execute( """CREATE TYPE IF NOT EXISTS raw.square (
                        x_min           varint,
                        y_min           varint,
                        val             varint,
                        frame_number    varint ); """ )
    
    # byteblock type def
    __session.execute( """CREATE TYPE IF NOT EXISTS raw.byteblock (
                        x               set<varint>,
                        y               set<varint>,
                        val             set<varint>,
                        side_length     varint );""" )
    
    
    
    # table definitions
    #-------------------
    
    
    # misfits table
    __session.execute( """CREATE TABLE IF NOT EXISTS raw.misfits (
                        errors      varchar,
                        device_id   varchar,
                        submit_time varint,
                        tarfile     varchar,
                        tarmember   varchar,
                        host        varchar,
                        message     blob,
                        PRIMARY KEY ( device_id, submit_time ) );""" ) 
    
    # exposure_blocks table
    __session.execute( """CREATE TABLE IF NOT EXISTS raw.exposure_blocks (
                        device_id           varchar,
                        submit_time         varint,
                        tarfile             varchar,
                        tarmember           varchar,
                        host                varchar,
                        user_id             varint,
                        app_code            varchar,
                        remote_addr         inet,
    
                        precal_id           varint,
                        precal_id_hi        varint,
    
                        start_time          varint,
                        end_time            varint,
                        start_time_nano     varint,
                        end_time_nano       varint,
                        start_time_ntp      varint,
                        end_time_ntp        varint,
    
                        gps_lat             double,
                        gps_lon             double,
                        gps_altitude        double,
                        gps_accuracy        double,
                        gps_fixtime         varint,
                        gps_fixtime_nano    varint,
                        
                        battery_temp        varint, 
                        battery_end_temp    varint, 
                        daq_state           varchar, 
                        res_x               varint, 
                        res_y               varint, 
    
                        L1_thresh           varint, 
                        L2_thresh           varint, 
                        L0_conf             varchar,
                        L1_conf             varchar,
                        L2_conf             varchar,
                        L0_processed        varint,
                        L1_processed        varint,
                        L2_processed        varint,
                        L0_pass             varint,
                        L1_pass             varint,
                        L2_pass             varint,
                        L0_skip             varint,
                        L1_skip             varint,
                        L2_skip             varint,
                        frames_dropped      varint,
    
                        hist                set<varint>,
                        xbn                 varint,
                        aborted             boolean,
    
                        block_uuid          uuid,
                        n_events            varint,
    
                        PRIMARY KEY ( device_id, block_uuid, start_time, gps_altitude, gps_lat, gps_lon ) );""" )
    
    # events table
    __session.execute( """CREATE TABLE IF NOT EXISTS raw.events (
                        device_id           varchar,
                        submit_time         varint,
                        tarfile             varchar,
                        tarmember           varchar,
                        host                varchar,                        
                        user_id             varint,
                        app_code            varchar,
                        remote_addr         inet,

                        run_id              varint,
                        run_id_hi           varint,
                        precal_id           varint,
                        precal_id_hi        varint,
                                            
                        start_time          varint,
                        end_time            varint,
                        start_time_nano     varint,
                        end_time_nano       varint,
                        start_time_ntp      varint,
                        end_time_ntp        varint,
                        
                        timestamp           varint,
                        timestamp_nano      varint,
                        timestamp_ntp       varint,
                        timestamp_target    varint,    
                        
                        gps_lat             double,
                        gps_lon             double,
                        gps_altitude        double,
                        gps_accuracy        double,
                        gps_fixtime         varint,
                        gps_fixtime_nano    varint,
    
                        battery_temp        varint,
                        pressure            double,
                        orient_x            double,
                        orient_y            double,
                        orient_z            double,
                                            
                        daq_state           varchar, 
                        res_x               varint,
                        res_y               varint, 
                        L1_thresh           varint, 
                        L2_thresh           varint, 
                        L0_conf             varchar,
                        L1_conf             varchar,
                        L2_conf             varchar,
                        L0_processed        varint,
                        L1_processed        varint,
                        L2_processed        varint,
                        L0_pass             varint,
                        L1_pass             varint,
                        L2_pass             varint,
                        L0_skip             varint,
                        L1_skip             varint,
                        L2_skip             varint,
                        frames_dropped      varint,
                        aborted             boolean,
                        battery_start_temp  varint, 
                        battery_end_temp    varint,
                                            
                        avg                 double,
                        std                 double,
    
                        hist                set<varint>,
                        xbn                 varint,
    
                        block_uuid          uuid,
                        byte_block          frozen <byteblock>, 
                        pixels              set<frozen <pixel>>,            
                        zero_bias           frozen <square>,
                        PRIMARY KEY ( device_id, block_uuid, timestamp, gps_altitude, gps_lat, gps_lon ) );""" )
    
    # run_configs table
    __session.execute( """CREATE TABLE IF NOT EXISTS raw.run_configs (
                        device_id           varchar,
                        submit_time         varint,
                        tarfile             varchar,
                        tarmember           varchar,
                        host                varchar,                        
                        user_id             varint,
                        app_code            varchar,
                        remote_addr         inet,
    
                        run_id_hi           varint,
                        run_id              varint,
    
                        start_time          varint,
                        crayfis_build       varchar,
                        hw_params           varchar,
                        os_params           varchar,
                        camera_params       varchar,
                        camera_id           varint,
                        PRIMARY KEY ( device_id ) );""" )
    
    # calibration_results table
    __session.execute( """CREATE TABLE IF NOT EXISTS raw.calibration_results (
                        device_id           varchar,
                        submit_time         varint,
                        tarfile             varchar,
                        tarmember           varchar,
                        host                varchar,                                                
                        user_id             varint,
                        app_code            varchar,
                        remote_addr         inet,
    
                        run_id              uuid,
                        run_id_hi           varint,
                        
                        start_time          varint,
                        end_time            varint,
    
                        hist_pixel          set<varint>,
                        hist_l2pixel        set<varint>,
                        hist_maxpixel       set<varint>,
                        hist_numpixel       set<varint>,
                        PRIMARY KEY ( device_id ) );""" )
    
    # precalibration_results table
    __session.execute( """CREATE TABLE IF NOT EXISTS raw.precalibration_results (
                        device_id           varchar,
                        submit_time         varint,
                        tarfile             varchar,
                        tarmember           varchar,
                        host                varchar,                                                
                        user_id             varint,
                        app_code            varchar,
                        remote_addr         inet,
                        
                        run_id              varint,
                        run_id_hi           varint,
                        precal_id           varint,
                        precal_id_hi        varint,
                        
                        start_time          varint,
                        end_time            varint,
    
                        weights             set<double>,
    
                        sample_res_x        varint,
                        sample_res_y        varint,
                        interpolation       varint,
                        battery_temp        varint,
                        
                        compressed_weights  varchar,
                        compressed_format   varchar,
                        
                        second_hist         set<varint>,
                        hotcell             set<varint>,
                        res_x               varint,
                        PRIMARY KEY ( device_id ) );""" )
    
    

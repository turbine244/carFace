import time
import module.status as stat

def engineWorks() :
    while (stat.is_drive_active == True) :
        target_rpm = stat.idle_rpm + (stat.max_rpm - stat.idle_rpm) * (stat.throttle / 100)
        stat.rpm += (target_rpm - stat.rpm) * stat.response_rate
        
        time.sleep(0.01)
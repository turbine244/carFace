import time
import threading as th
import module.status as stat

def safeDrive() :    
    stat.interrupt_throttle = True
    stat.message = "감속 중"
    
    while ((stat.rpm.__floor__() > stat.idle_rpm.__floor__())) :
        stat.throttle *= 0.90
        time.sleep(0.01)

    stat.interrupt_throttle = False
    stat.message = ""
    stat.is_assist_active = False
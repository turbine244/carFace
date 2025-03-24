import time
import threading as th
import module.status as stat
import module.detect_face as df

prev_throttle = 0

def detect_acc() :
    global prev_throttle
    
    prev_throttle = stat.throttle
    
    while (stat.is_drive_active == True) :
        if stat.throttle - prev_throttle > 50 and stat.rpm > 2500:
            stat.message = "급가속"
            df.detect_face()
        else :
            stat.message = ""
            
        prev_throttle = stat.throttle
        time.sleep(0.1)
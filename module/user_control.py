import time
import keyboard
import module.status as stat
import module.driveAssist as assist

def user_accelerate() :
    while (stat.is_drive_active == True) :
                
        while (stat.interrupt_throttle == True) :
            time.sleep(0.01)
        
        if (keyboard.is_pressed("a")) :
            stat.throttle -= 50
            
        if (keyboard.is_pressed("s")) :
            stat.throttle -= 1
            
        if (keyboard.is_pressed("d")) :
            stat.throttle += 1
            
        if (keyboard.is_pressed("f")) :
            stat.throttle += 100            
        
        if (stat.throttle < 0) :
            stat.throttle = 0
        if (stat.throttle > 100) :
            stat.throttle = 100
            
        time.sleep(0.1)
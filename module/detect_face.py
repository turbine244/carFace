import threading as th
import time
import module.status as stat
import module.driveAssist as assist

def detect_face() :
   if (True) :
        stat.is_assist_active = True
        stat.message = "급발진"     
        
        thread_assist = th.Thread(target=assist.safeDrive)       
        thread_assist.start()
        thread_assist.join()
        return
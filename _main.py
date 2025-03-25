import threading as th
import time

import module.car as car
import module.status as stat
import module.detect_acc as da
import module.user_control as uc

import module.model_face as model

model.network.summary() 
    
listThread = []
listThread.append(th.Thread(target=stat.print_dashboard))
listThread.append(th.Thread(target=car.engineWorks))
listThread.append(th.Thread(target=uc.user_accelerate))
listThread.append(th.Thread(target=da.detect_acc))

for thread in listThread :
    thread.start()

time.sleep(60)
stat.is_drive_active = False
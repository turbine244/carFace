import threading as th
import time
import module.detect_acc as da

is_drive_active = True
is_drive_abnormal = False
is_assist_active = False

interrupt_throttle = False

throttle = 0.0
rpm = 800.0

max_rpm = 7000
idle_rpm = 800
response_rate = 0.1

message = ""

def print_dashboard() :
    while (is_drive_active == True) :
        print("throtle %d %% (prev %d %%)   %d RPM    %s" % (throttle, da.prev_throttle, rpm, message))
        time.sleep(0.01)
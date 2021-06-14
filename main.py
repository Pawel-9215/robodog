# servo motor control for robot

from machine import Pin, PWM
import utime

frontWheel_servo = PWM(Pin(0))
frontWheel_servo.freq(50)

backwheel_dir_for = Pin(15, Pin.OUT)
backwheel_dir_back = Pin(13, Pin.OUT)
backwheel_pwm = PWM(Pin(14))
backwheel_pwm.freq(50)

"""
Lets figure that out - duty
1350 - 0[deg]
8200 - 180[deg]
8200-1350 = 6850
value = 1350 + Xdeg * (6850/180)
"""

def move_forward():
    backwheel_dir_back.value(0)
    backwheel_dir_for.value(1)
    
def move_backward():
    backwheel_dir_for.value(0)
    backwheel_dir_back.value(1)

while True:
    #direction = int(1350 + int(input()) * (6858/180))
    #frontWheel_servo.duty_u16(direction)
    dir12 = input()
    if dir12 == "w":
        move_forward()
    elif dir12 == "s":
        move_backward()
        
    else:
        direction = int(dir12)
        backwheel_pwm.duty_u16(int(direction*direction))
        utime.sleep(0.02)

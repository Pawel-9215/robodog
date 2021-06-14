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

def move_backward():
    backwheel_dir_back.value(0)
    backwheel_dir_for.value(1)
    
def move_forward():
    backwheel_dir_for.value(0)
    backwheel_dir_back.value(1)
    
def set_speed(speed):
    backwheel_pwm.duty_u16(int(speed*speed))
    
def turn_left():
    direction_fw = int(1350 + 45 * (6858/180))
    frontWheel_servo.duty_u16(direction_fw)
    move_forward()
    set_speed(180)
    utime.sleep(2)
    set_speed(0)
    
def turn_right():
    direction_fw = int(1350 + (90+45) * (6858/180))
    frontWheel_servo.duty_u16(direction_fw)
    move_forward()
    set_speed(180)
    utime.sleep(2)
    set_speed(0)
    
def reset_front():
    direction_fw = int(1350 + 90 * (6858/180))
    frontWheel_servo.duty_u16(direction_fw)
    

while True:
    #direction = int(1350 + int(input()) * (6858/180))
    #frontWheel_servo.duty_u16(direction)
    dir12 = input()
    
    if dir12 == "w":
        reset_front()
        move_forward()
        set_speed(160)
        utime.sleep(2)
        set_speed(0)
        
    elif dir12 == "s":
        reset_front()
        move_backward()
        set_speed(160)
        utime.sleep(2)
        set_speed(0)
    
    elif dir12 == "a":
        turn_left()
        
    elif dir12 == "d":
        turn_right()
        





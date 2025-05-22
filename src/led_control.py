from hal import hal_led as led
from threading import Thread
from time import sleep

from hal import hal_keypad as keypad

def led_thread():
    global delay
    delay = 0
    while(True):
        print("DELAY = ", delay)
        if delay != 0:
            led.set_output(20,1)
            sleep(delay)
            led.set_output(20, 0)
            sleep(delay)
        # Added the else condition to include the sleep() to slow down the while loop.
        else:
            sleep(0.5)   



def led_control_init():
    global delay
    led.init()
    t1 = Thread(target=led_thread)
    t1.start()
    #Set initial LED blinking every 1 second after Thread starts
    delay = 1


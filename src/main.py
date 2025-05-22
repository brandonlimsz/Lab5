from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import led_control as LED

#Empty list to store sequence of keypad presses
password = []

lcd = LCD.lcd()
lcd.lcd_clear()

#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    password.append(key)
    print(password)
    if key==1:
        LED.delay=1 # Blink LED every 1 second
        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1)
        lcd.lcd_display_string("Blinking LED", 2)
    if key==0:
        LED.delay=0 # Off LED
        lcd.lcd_display_string("LED Control", 1)
        lcd.lcd_display_string("LED off", 2)


def main():
    # Initialize LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()

    # Display something on LCD
    lcd.lcd_display_string("Lab 5", 1)

    # Initialize the HAL keypad driver
    keypad.init(key_pressed)
    LED.led_control_init()

    # Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

    # Display the instruction for user
    lcd.lcd_clear()
    lcd.lcd_display_string("LED Control", 1)
    lcd.lcd_display_string("0:Off  1:Blink", 2)



# Main entry point
if __name__ == "__main__":
    main()

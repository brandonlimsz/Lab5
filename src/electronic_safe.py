from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import led_control as LED
import time

#Empty list to store sequence of keypad presses
global password   # A list to store the keys pressed
global PIN_done   # A flag of whether user has pressed '#' as "ENTER"
global NewKeyPressed # A flag of whether a new key has been pressed.

#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    global PIN_done
    global password
    global NewKeyPressed
    if key=='#':  # User pressed '#' = <ENTER>
        PIN_done = True
    else:   # PIN not done. Append key pressed to password string
        password.append(key)
        PIN_done = False
    NewKeyPressed = True


def main():
    global PIN_done
    global password
    global NewKeyPressed
    CORRECT_PIN = [3,4,5,6]   # This is the PIN to unlock the safe.
    PIN_done = False

    password = []
    trial_count = 0
    PIN_correct = False
    NewKeyPressed = False

    # Initialize LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()

    # Display instruction on LCD
    #----------------------"1234567890123456"
    lcd.lcd_display_string("Safe Lock       ", 1)
    lcd.lcd_display_string("Enter PIN:      ", 2)

    # Initialize the HAL keypad driver
    keypad.init(key_pressed)

    # Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

    # Waiting for user to enter PIN
    while trial_count <3 and PIN_correct == False:
        if NewKeyPressed == True:
            NewKeyPressed = False
            if PIN_done == True:
                # Check whether PIN is correct
                if password == CORRECT_PIN: # Correct PIN has been entered
                    lcd.lcd_display_string("Safe unlocked   ", 2)
                    time.sleep(2)
                    PIN_correct = True  # Exit the While loop
                else:   # Wrong PIN
                    lcd.lcd_display_string("Wrong PIN       ", 2)
                    time.sleep(2)
                    trial_count += 1
                    if trial_count<3:   # More trial is allowed
                        lcd.lcd_display_string("Enter PIN:      ", 2)
                        password = []  # Reset password
                        PIN_done = False
                    else:
                        lcd.lcd_display_string("Failed 3 times! ", 2)
                        time.sleep(2)                       

            else:  # PIN_done == False. Still not end of PIN, collect more keys
                # Print a string of '*'s to represent the keys pressed
                # Also fill the rest of LCD line 2 with spaces.
                n = len(password)
                star_str = ('*'*n) + (' '*(16-n))  # LCD has 16 chars per line
                lcd.lcd_display_string(star_str, 2)

    lcd.lcd_display_string("Terminated      ", 2)
    #time.sleep(3)



# Main entry point
if __name__ == "__main__":
    main()

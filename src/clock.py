from hal import hal_lcd as LCD
import time


def main():
    lcd = LCD.lcd()
    show_colon = 1

    lcd.lcd_clear()
    # Display something on LCD
    lcd.lcd_display_string("Lab 5 Ex3", 1)
    lcd.lcd_display_string("Clock", 2)
    time.sleep(2)
    lcd.lcd_clear()
    time_keeper = time.time() # This is the timer for 0.5 sec

    while True:
        # Read the local time
        local_time = time.localtime() # get struct_time
        if show_colon == 1:
            time_string = time.strftime("%H:%M:%S", local_time)
            #time_string = time.strftime("%l:%M:%S %p", local_time)  # Show hh:mm:ss PM
            show_colon = 0
        else:
            time_string = time.strftime("%H %M %S", local_time)
            #time_string = time.strftime("%l %M %S %p", local_time)   # Show hh:mm:ss PM
            show_colon = 1  
        date_string = time.strftime("%d-%m-%Y", local_time)
        #date_string = time.strftime("%d-%b-%Y", local_time)   # Show dd-mmm-yyyy
        # Display the Date and Time
        lcd.lcd_display_string(time_string, 1)
        lcd.lcd_display_string(date_string, 2)
        
        # Wait until 0.5 sec has lapsed
        while time.time() < (time_keeper + 0.5):
            time.sleep(0.01)   # A suitable delay before next time checking
        time_keeper += 0.5   # Update the next expire time



# Main entry point
if __name__ == "__main__":
    main()


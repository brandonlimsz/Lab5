from hal import hal_servo as SERVO
from hal import hal_adc as ADC
from hal import hal_lcd as LCD
import time


def main():
    SERVO.init()
    ADC.init()
    lcd = LCD.lcd()

    lcd.lcd_clear()
    # Display something on LCD
    lcd.lcd_display_string("Lab 5 Ex2", 1)
    lcd.lcd_display_string("ADC and Servo", 1)

    while True:
        # Read the potentiometer value from the ADC
        adc_value = ADC.get_adc_value(1)
        # Turn the servo control
        angle = -180.0*adc_value/1023.0 + 180.0
        print("ADC, Angle : "+ str(adc_value) + "\t" + str(round(angle,1)))
        # Control the servo motor
        SERVO.set_servo_position(angle)
        time.sleep(0.2)   # A small delay to reduce the rate of reading adc/control servo


# Main entry point
if __name__ == "__main__":
    main()

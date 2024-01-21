import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pins for the LEDs
led_pins = [37, 35, 33, 31, 29, 23, 21]

# Set up the GPIO pins for output
for pin in led_pins:

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # Turn off all LEDs initially

def turn_on_led(led_number):
    # Turn off all LEDs
    for pin in led_pins:
        GPIO.output(pin, GPIO.LOW)

    # Turn on the specified LED
    if 1 <= led_number <= 7:
        GPIO.output(led_pins[led_number - 1], GPIO.HIGH)

# Example variable value (replace with your variable)
variable_value = 7

# Turn on the corresponding LED based on the variable value
turn_on_led(variable_value)

# Wait for some time (you can adjust the delay as needed)
time.sleep(5)

# Clean up GPIO
GPIO.cleanup()
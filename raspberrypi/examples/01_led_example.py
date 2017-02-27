"""

This example will blink an LED every second.

Required components:
    - 1 LED
    - 1 330ohm resistor
    - 2 wires
    - breadboard
    - Pi Cobbler breakout board and cable

Instructions:
    1. Connect the Pi Cobbler to the Raspberry Pi and the breadboard
    2. Connect one wire from GND to the blue rail on the breadboard
    3. Connect another wire from #17 to the positive (long) lead of the LED
    4. Connect a resistor from the negative (short) lead of the LED to GND
    5. Click Run -> Run Module or press F5

"""

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# The pin we will be connecting to our LED
ledPin = 17

# Tell the Pi that we are using the pin as an output
# to turn the LED on or off
GPIO.setup(ledPin, GPIO.OUT)

print 'Running program...'

# The current status of the LED
ledIsOn = True

# This is a loop. The instructions preceeding the loop
# will run until forcefully terminated
while True:

    if ledIsOn == True:
        # Turn on the LED
        GPIO.output(ledPin, GPIO.HIGH)
    else:
        # Turn off the LED
        GPIO.output(ledPin, GPIO.LOW)

    # Tell the Pi to switch the LED on or off
    ledIsOn = not ledIsOn

    # Do nothing for 1 second
    time.sleep(1)

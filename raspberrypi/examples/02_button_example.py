"""

This example will tell us the status of a button every second.

Required components:
    - 1 push button
    - 2 wires
    - breadboard
    - Pi Cobbler breakout board and cable

Instructions:
    1. Connect the Pi Cobbler to the Raspberry Pi and the breadboard
    2. Connect a wire from pin #18 to one side of the button
    3. Connect a wire from the other side of the button to 3V3
    4. Click Run -> Run Module or press F5

"""

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# The pin we will be connecting to our button
button = 18

# Tell the Pi that we are using the pin as an input
# to read the status of a push button
GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)

print 'Running program...'

# This is a loop. The instructions preceeding the loop
# will run until forcefully terminated
while True:

    # Read the status (voltage) of the pin
    buttonState = GPIO.input(button)

    if buttonState == GPIO.HIGH:
        print ('Button pressed')
    else:
        print ('Button released')

    # Do nothing for 1 second
    time.sleep(1)

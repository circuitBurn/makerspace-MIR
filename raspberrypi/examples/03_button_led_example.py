"""

This example will blink an LED every second.

Required components:
    - 1 LED
    - 1 330ohm resistor
    - 1 pushbutton
    - 2 wires
    - breadboard
    - Pi Cobbler breakout board and cable

Instructions:
    1. Connect the Pi Cobbler to the Raspberry Pi and the breadboard
    2. Connect one wire from GND to the blue rail on the breadboard
    3. Connect another wire from #17 to the positive (long) lead of the LED
    4. Connect a resistor from the negative (short) lead of the LED to GND
    5. Connect a wire from pin #18 to one side of the button
    6. Connect a wire from the other size of the button to 3V3
    5. Click Run -> Run Module or press F5

"""

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# The pin we will be connecting to our LED
ledPin = 17

# The pin we will be connecting to our button
button = 18

# Tell the Pi that we are using the pin as an output
# to turn the LED on or off
GPIO.setup(ledPin, GPIO.OUT)

# Tell the Pi that we are using the pin as an input
# to read the status of a push button
GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)

print 'Running program...'


# This is a loop. The instructions preceeding the loop
# will run until forcefully terminated
while True:

    # Read the status (voltage) of the pin
    buttonIsPressed = GPIO.input(button)

    GPIO.output(ledPin, buttonIsPressed)

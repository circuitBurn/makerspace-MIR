// NeoPixel Ring chaser

#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif

// Which pin on the Arduino is connected to the NeoPixels?
#define PIN            6

// How many individual NeoPixels are on the ring?
#define NUMPIXELS      12


// When we setup the NeoPixel library, we tell it how many pixels, and which pin to use to send signals.
// Note that for older NeoPixel strips you might need to change the third parameter--see the strandtest
// example for more information on possible values.
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

int delayval = 100;

int RED = 0;
int GREEN = 0;
int BLUE = 0;

void setup() {
#if defined (__AVR_ATtiny85__)
  if (F_CPU == 16000000) clock_prescale_set(clock_div_1);
#endif
  pixels.begin();
  pixels.setBrightness(64);
}

void loop() {

  // Turn off all of the LEDs in the ring
  clear();

  // Randomize the colour choice each cycle
  RED   = random(0, 150);
  GREEN = random(0, 150);
  BLUE  = random(0, 150);

  // Update each pixel in the ring with a delay to simulate a "chase" effect
  for (int i = 0; i < NUMPIXELS; i++) {
    pixels.setPixelColor(i, pixels.Color(RED, GREEN, BLUE));  
    pixels.show();
    delay(delayval);
  }
  
}

/**
 * Clear the neopixels
 */
void clear() {
  for( int i = 0; i<NUMPIXELS; i++){
    pixels.setPixelColor(i, 0x000000); 
    pixels.show();
  }
}

import tealight
import board
import neopixel
import RPi.GPIO as GPIO

pixel_pin = board.D18

# The number of lights in your neopixel strand
num_pixels = 7

# Are these neopixels RGB, or RGBW/RGBWW?
#
# RGB, use this one:
# four_color_neopixels = False
#
# RGBW/RGBWW, use this one:
four_color_neopixels = True

# Sometimes the color order of the Neopixel is RGB, sometimes it's GRB, etc.
# If the color of the candle flame looks weird, say Green, switch the order :)
led_order = neopixel.GRBW

strip = neopixel.NeoPixel(
    pin=pixel_pin,
    n=num_pixels,
    brightness=1,
    auto_write=False,
    pixel_order=led_order
)

# A steady candle is cool, but a candle that occasionally flickers is cooler.
# You can set the value between 1 - 10.  The lower the value, the more likely
# the candle will switch to the flickering pattern.
flicker_probability = 8

candle = tealight.candle(
    pixel = 0,
    neopixel_strip = strip,
    four_color_neopixels = four_color_neopixels
)
candle.cleanup()

# The candle is playing back the normal/flicker patterns from the .csv files.
# The CSV files were recorded at 175Hz (2 millisecond intervals.) The patterns
# don't really look right if you play them back at a slower (or faster)
# interval.
#
# To make things look correct, you need to call the update method every pass
# through the loop.  Don't add a time.sleep to this loop, it tends to mess up
# the playback.  The update method internally keeps track of how much time has
# passed since the neopixel was last updated, and it will update it after 2
# milliseconds has passed.
try:
    while True:
        candle.update(chance_flicker = flicker_probability)

except KeyboardInterrupt:	   # When 'Ctrl+C' is pressed,

    # Call the cleanup method to turn the led off
    candle.cleanup()
    exit()

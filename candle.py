import tealight
import board
import neopixel
import RPi.GPIO as GPIO

pixel_pin = board.D18
num_pixels = 7
four_color_neopixels = True
led_order = neopixel.GRBW

strip = neopixel.NeoPixel(
    pin=pixel_pin,
    n=num_pixels,
    brightness=1,
    auto_write=False,
    pixel_order=led_order
)

# Candle Color Variables (What color is our flame?)
red = 255
green = 127
blue = 10

flicker_probability = 8

candle = tealight.candle(
    pixel = 0,
    neopixel_strip = strip,
    interval = .0020,
    four_color_neopixels = four_color_neopixels,
    red = red,
    green = green,
    blue = blue
)
candle.cleanup()

try:
    while True:
        candle.update(chance_flicker = flicker_probability)

except KeyboardInterrupt:	   # When 'Ctrl+C' is pressed,
    candle.cleanup()
    exit()

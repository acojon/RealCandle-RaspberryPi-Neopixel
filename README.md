# RealCandle-RaspberryPi-Neopixel

Based on coldcpu's excellent [“Reverse engineering” a real candle](https://cpldcpu.wordpress.com/2016/01/05/reverse-engineering-a-real-candle/) and forked from [RealCandle](https://github.com/cpldcpu/RealCandle)

Like many folks, one of my first projects with a micro controller thingie, was
 to make an electronic candle.  My micro controller of choice is the Raspberry
 Pi.  When I was looking for examples to help me out, most of the examples are
 written for an Arduino (or related micro controller) and didn't really help me
 out.  I wasn't able to come up with a flickering candle pattern on my own that
 I liked, and stealing patterns from other projects (once I understood how a
 given project worked,) didn't yield patterns I liked either.  And then I found
 the project linked above!

I used the .csv files from the project, and some other clues, and by playing
 back the patterns encoded in the two .csv files, I got an artificial candle
 that I really like!

In my own implementation, I've included a switch to turn the candle on and off,
 MQTT functionality so that the home automation software can turn the candle on
 and off, and the flicker probability changes as the local wind speed changes.
 That kind of script is very much customized to my own environment, and it may
 not be helpful to someone who is looking for a LED candle to run on a
 Raspberry Pi.  This repository should make for a great starting point to make
 your own candle, and add the additional functionality that you desire.

## Setup

The code uses the Adafruit CircuitPython libraries to manage the Neopixel.  The python code relies on a couple supporting libraries

``` bash
pip3 install adafruit-blinka rpi_ws281x adafruit-circuitpython-neopixel
```

Once the installation is complete, clone the repository:

```bash
git clone https://github.com/acojon/RealCandle-RaspberryPi-Neopixel
```

__Note:__ At this point, you can run the test
[script](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/master/examples/rpi_neopixel_simpletest.py)
from Adafruit's repository to test that the Neopixels are properly wired into
the Raspberry Pi and that things are working properly.

Change into the repository folder, and start the demo script:

```bash
cd RealCandle-RaspberryPi-Neopixel

python3 candle.py
```

## How to use the tealight module

These instructions are written with the understanding that you have already
setup a Raspberry Pi, you can SSH into it, and that you have one or more
Neopixel lights properly connected to your Raspberry Pi.  Hint: Here's a good
[reference](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview)

The module was written to allow you to setup each individual light on a
Neopixel strip as a candle.  To do this, you create a candle object and set the
pixel number to represent the corresponding light.  What I do is use individual
Neopixel led's on a breakout board, and then solder wires to create a string of
5 - 7 neopixels, each with 6-ish inches of wire between them.  I then place the
neopixels into tealight holders, and set them up on a shelf.  Each candle
object will appear to burn/flicker independent of the others while they're all
managed with one script.

There is probably an upper practical limit to the number of candles, I don't
know what that number is :)

There are a few methods for the tealight module.  Check out the candle.py
script and the tealight module for an example use case.

### __setup__

When you're initializing a candle object, you need to include a number of
parameters:

#### pixel

Which Neopixel on your strip of Neopixels does the candle object manage?
Neopixel number 0? Number 3?

#### neopixel_strip

The Neopixel object that represents the entire strip of Neopixels.  (You
 initialized that a little earlier in the script)

#### interval

How much time must pass before the candle object will update the Neopixel to
the next brightness value in the pattern?  Defaults to .0020 seconds. I
 recommend you take the default value :)

#### four_color_neopixels

True or False?  Is this a  3 color or a 4 color neopixel?

#### red

The default red value for the candle.  Defaults to 255.  Change it if you want
your candle to burn a different color :)

#### green

The default green value for the candle.  Defaults to 127.  Change it if you want
your candle to burn a different color :)

#### blue

The default red value for the candle.  Defaults to 10.  Change it if you want
your candle to burn a different color :)

#### An example:

```python3
# This initializes the candle object, for the first Neopixel in the strip, and
# the strip Neopixels have four colors
candle = tealight.candle(
    pixel = 0,
    neopixel_strip = strip,
    four_color_neopixels = True
)

# This initializes the candle object, for the 4th Neopixel in the strip, the
# strip Neopixels have three colors, and the candle will have a Green-Blue-Ish
# color.
candle = tealight.candle(
    pixel = 3,
    neopixel_strip = strip,
    four_color_neopixels = False,
    red = 10,
    green = 255,
    blue = 128
)
```

### cleanup

Call this method when you want to turn off the Neopixel connected to the
 candle object.  I like to use these as part of the shutdown/quit sequence.

### update

Every pass through your loop, call this method.  Do not include a sleep in your
 loop, as this will mess with the timing of the candle pattern.
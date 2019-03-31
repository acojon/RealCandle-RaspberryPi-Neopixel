# RealCandle-RaspberryPi-Neopixel

Based on coldcpu's excellent [“Reverse engineering” a real candle](https://cpldcpu.wordpress.com/2016/01/05/reverse-engineering-a-real-candle/) and forked from [RealCandle](https://github.com/cpldcpu/RealCandle)

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

#### pixel

#### neopixel_strip

#### interval

#### four_color_neopixels

#### red

#### green

#### blue

### cleanup

### update
# RealCandle-RaspberryPi-Neopixel

Based on coldcpu's excellent [“Reverse engineering” a real candle](https://cpldcpu.wordpress.com/2016/01/05/reverse-engineering-a-real-candle/) and forked from [RealCandle](https://github.com/cpldcpu/RealCandle)

## Setup

The code uses the Adafruit CircuitPython libraries to manage the Neopixels.  The python code relies on a couple supporting libraries

``` bash
pip3 install adafruit-blinka rpi_ws281x adafruit-circuitpython-neopixel
```
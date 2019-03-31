import csv
import neopixel
import os.path
from random import randint
import statistics
import time

class candle():

    ### File Locations ###
    flicker_burn_file = "./candle1.csv"
    normal_burn_file = "./candle2.csv"

    red = 0
    green = 0
    blue = 0

    # Declare our internal variables for the object.
    cycle_tracker = 0
    cycle_tracker_reset = 0
    flicker_brightness = []
    four_color_neopixels = False
    interval = ""
    last_update = 0
    neopixel_strip = 0
    normal_brightness = []
    pixel = 0

    # Initialize our state tracking variables.
    active_pattern = "choose"
    first_pass = True
    escape_from_flicker = False
    escape_from_normal = 0
    time_in_flicker = 0
    time_in_normal = 0

    # Initialize
    def __init__(
        self,
        pixel,
        neopixel_strip,
        interval = .0020,
        four_color_neopixels = False,
        red = 255,
        green = 127,
        blue = 10
    ):

        # Initialize the variables

        self.pixel = pixel
        self.neopixel_strip = neopixel_strip
        self.interval = interval
        self.red = red
        self.green = green
        self.blue = blue

        self.four_color_neopixels = four_color_neopixels

        # Generate the burn brightness pattern tuples.
        self.normal_brightness = self.read_csv_file(self.normal_burn_file)
        self.flicker_brightness = self.read_csv_file(self.flicker_burn_file)
        self.cycle_tracker_reset = len(self.normal_brightness) - 1

    def build_candle_array(self, data):
        maplen = 200
        scale = 0.8 * maplen / statistics.median(data)
        temp_tuple = []
        for element in data:
            brightness = scale * element + 1
            current_red = int(self.red * brightness/256)
            if (current_red > 255):
                current_red = 255
            current_green = int(self.green * brightness/256)
            if (current_green > 255):
                current_green = 255
            current_blue = int(self.blue * brightness/256)
            if (current_blue > 255):
                current_blue = 255
            if (self.four_color_neopixels):
                temp_tuple.append((current_red, current_green, current_blue))
            else:
                temp_tuple.append((current_green, current_red, current_blue))
        return temp_tuple

    def read_csv_file(self, file_name):
        data_tracker = []
        if os.path.isfile(file_name):
            with open(file_name) as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                        data_tracker.append(float(row[1]))
        else:
            print ("Can't read: ", file_name)
            exit(1)	
        final_tuple = self.build_candle_array(data_tracker)
        return final_tuple

    def cleanup(self):
        # Set the LED to black; i.e., turn off the current LED.
        if (self.four_color_neopixels):
            self.neopixel_strip[self.pixel] = (0,0,0,0)
        else:
            self.neopixel_strip[self.pixel] = (0,0,0)
        self.neopixel_strip.show()

    def reset(self):
        # Reset the internal state to that of a new
        # object.
        self.active_pattern = "choose"
        self.first_pass = True
        self.last_update = time.time()

    def update(self,chance_flicker):
        if (self.first_pass):
            rand_sleep = (randint(0,2)) + (randint(0,1000)/1000)
            self.last_update += rand_sleep
            self.first_pass = False
        if (time.time() - self.last_update) > self.interval:
            # Time to update
            self.last_update = time.time()
            if self.active_pattern == "normal":
                if self.time_in_normal == 0 and self.escape_from_normal == 0:
                    self.escape_from_normal = randint(500,1500)
                    # Pick a random starting point in the normal_brightness tuple
                    self.cycle_tracker = randint(0,(len(self.normal_brightness) - 1))
                elif self.time_in_normal > self.escape_from_normal:
                    self.time_in_normal = 0
                    self.escape_from_normal = 0
                    self.active_pattern = "choose"
                else:
                    # Do Normal Burn stuff
                    self.time_in_normal += 1
                    self.normal()
            elif self.active_pattern == "flicker":
                # Do flicker Stuff
                if self.escape_from_flicker:
                    self.escape_from_flicker = False
                    self.active_pattern = "choose"
                else:
                    self.flicker()
            elif self.active_pattern == "choose":
                # Choose your own adventure!
                if randint(1,10) > chance_flicker:
                    self.active_pattern = "flicker"
                else:
                    self.active_pattern = "normal"

    def normal(self):
        if (self.four_color_neopixels):
            self.neopixel_strip[self.pixel] = (
                (self.normal_brightness[self.cycle_tracker][0]),
                (self.normal_brightness[self.cycle_tracker][1]),
                (self.normal_brightness[self.cycle_tracker][2]),
                0
            )
        else:
            self.neopixel_strip[self.pixel] = (
                (self.normal_brightness[self.cycle_tracker][0]),
                (self.normal_brightness[self.cycle_tracker][1]),
                (self.normal_brightness[self.cycle_tracker][2])
            )
        self.neopixel_strip.show()
        self.cycle_tracker += 1
        if (self.cycle_tracker > self.cycle_tracker_reset):
            self.cycle_tracker = 0
            self.first_pass = True

    def flicker(self):
        if (self.four_color_neopixels):
            self.neopixel_strip[self.pixel] = (
                self.flicker_brightness[self.cycle_tracker][0],
                self.flicker_brightness[self.cycle_tracker][1],
                self.flicker_brightness[self.cycle_tracker][2],
                0
            )
        else:
            self.neopixel_strip[self.pixel] = (
                self.flicker_brightness[self.cycle_tracker][0],
                self.flicker_brightness[self.cycle_tracker][1],
                self.flicker_brightness[self.cycle_tracker][2]
            )
        self.neopixel_strip.show()
        self.cycle_tracker += 1
        if (self.cycle_tracker > self.cycle_tracker_reset):
            self.cycle_tracker = 0
            self.first_pass = True
            self.escape_from_flicker = True

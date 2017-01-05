#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
from rgbmatrix import RGBMatrix
from pprint import pprint
from character import Character
import json
import time
import socket

global row, chain, column, canvas, color

class MainMatrix(SampleBase):
    
    def __init__(self, *args, **kwargs):
        super(MainMatrix, self).__init__(*args, **kwargs)

# Main function
if __name__ == "__main__":
    while True:
        # initilzation of column, row and chain from json file
        with open('/var/www/html/led-controller/config.json') as data_file:    
            data = json.load(data_file)
        column = data['data'][0]['column']
        row = int(data['data'][1]['row'])
        chain = int(data['data'][2]['chain'])
        font = int(data['data'][4]['font'])
        font = 3 # font
        fx = 4 + font - 1 # length of x per char
        fy = 5 + (font - 1) * 2 # length of y per char
        canvas = RGBMatrix(row, chain, 1) # led matrix
        color = graphics.Color(255, 0, 0) # color
        # clean up and don't create a mess
        del data
        data_file.close()

        while True:
            sNumber = {} # screen number
            sNumSize = {} # amount of space needed for particular screen number
            with open('/var/www/html/led-controller/screen.json') as data_file:
                data = json.load(data_file)
            data_screen = data['data'][0]['screen']
            screen = len(data_screen)
            for num in range(1,screen+1):
                sNumber[num] = int(data['data'][num]['screen_' + str(num)])
                sNumSize[num] = len(data['data'][num]['screen_' + str(num)])
            parser = MainMatrix()
            con_char = Character(fx, fy, font)
            con_char.two(canvas, 10, 10, color)
            time.sleep(5)
            canvas.Clear()
            # check if required to restart for initilzation of chain,row, column
            # code for checking here.. (not written for now)
        # check for process
        if (not parser.process()):
            parser.print_help()




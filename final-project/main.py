# Yang Liu
# CMPT 120 D400
# April 7, 2022

import os
import pathlib

def main():
    menu_string = """
    1. Load Colour File
    2. Print All Colours
    3. Select Colour
    4. Find Closest Colour
    5. Display (Save) Colour Scheme
    0. Quit
    """
    
    print(menu_string)

    while True:
        user_input = input('Select an option: ')

        if user_input == '0':
            return
        elif user_input == '1':
            load_colour_file()

            return
        else:
            print('hello')

def load_colour_file():
    file = open("/Users/yangliu/Desktop/SFU/CMPT_120/final-project/colours.csv")

    colour_dictionary = {}
    with file as f:
        for line in file:
            print(line)
            # split_key_val = line.split(',', 1)
            # print(split_key_val)

main()

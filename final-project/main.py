# Yang Liu
# CMPT 120 D400
# April 7, 2022

import pathlib

colour_dictionary = {}

def main():
    print_menu()

    while True:
        user_input = input('Select an option: ')

        if user_input == '0':
            return
        elif user_input == '1':
            load_colour_file()
        elif user_input == '2':
            print_all_colours()
        elif user_input == '3':
            pass
        else:
            print_menu()

def load_colour_file():
    file = open(str(pathlib.Path(__file__).parent.resolve()) + '/colours.csv', 'r')
    
    for line in file:
        split_key_val = line.strip().split(',', 1)
        rgb_vals = split_key_val[1].split(',')
        hex_val = rgb_to_hex(rgb_vals)
        hex_string = ''.join(hex_val)
        value_list = [split_key_val[0], hex_string]

        key_tuple = tuple(rgb_vals)

        # Add key value pair to dictionary
        colour_dictionary[key_tuple] = value_list

    print(colour_dictionary)

def print_all_colours():
    print("{:<40} {:<10} {:<10} {:<10} {:<1}".format('Colour Name','Red','Green', 'Blue', 'Hex'))
    print("{:<40} {:<10} {:<10} {:<10} {:<1}".format('------------','----','------', '-----', '------'))

    for key in colour_dictionary:
        red = key[0]
        green = key[1]
        blue = key[2]
        colour_name = colour_dictionary[key][0].title()
        hex_val = colour_dictionary[key][1]
        print("{:<40} {:<10} {:<10} {:<10} {:<1}".format(colour_name, red, green, blue, hex_val))

def print_menu():
    menu_string = """
        1. Load Colour File
        2. Print All Colours
        3. Select Colour
        4. Find Closest Colour
        5. Display (Save) Colour Scheme
        0. Quit
        """
        
    print(menu_string)

def rgb_to_hex(rgb_list):
    hex_list = []

    for rgb_val in rgb_list:
        hex_val = hex(int(rgb_val))
        formatted_hex_val = hex_val.lstrip('0x')
        if formatted_hex_val == '':
            formatted_hex_val = '00'
        elif len(formatted_hex_val) == 1:
            formatted_hex_val = '0' + formatted_hex_val
        
        hex_list.append(formatted_hex_val)

    hex_list.insert(0, '#')

    return hex_list

main()

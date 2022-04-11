# Yang Liu
# CMPT 120 D400
# April 7, 2022

import pathlib
import cmpt120image

# Global Dictionary
colour_dictionary = {}

# Utility Functions

def print_menu():
    print('\n')
    print('1. Load Colour File')
    print('2. Print All Colours')
    print('3. Select Colour')
    print('4. Find Closest Colour')
    print('5. Display (Save) Colour Scheme')
    print('0. Quit')

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

def darken_pixel_colour(ls, percentage):
    darkened_list = []
    for pixel in ls:
        darkened_list.append(pixel * percentage)

    return darkened_list

def lighten_pixel_colour(ls, percentage):
    lightened_list = []
    for pixel in ls:
        new_pixel = pixel + (255 - pixel) * percentage
        lightened_list.append(new_pixel)

    return lightened_list

def complement_pixel_colour(ls):
    complement_pixel_list = []
    for pixel in ls:
        complement_pixel_list.append(255 - pixel)

    return complement_pixel_list

# Main Function

def main():
    while True:
        print_menu()
        user_input = input('Select an option: ')
        
        if user_input == '0':
            return
        elif user_input == '1':
            load_colour_file()
        elif user_input == '2':
            print_all_colours()
        elif user_input == '3':
            select_color()
        elif user_input == '4':
            find_closest_colour()
        elif user_input == '5':
            display_and_save_colour_scheme()
        else:
            print_menu()

# Part 1 - User Interface, Load and Print Dictionary

def load_colour_file():
    file = open(str(pathlib.Path(__file__).parent.resolve()) + '/colours.csv', 'r')
    
    for line in file:
        split_key_val = line.strip().split(',', 1)
        rgb_vals = split_key_val[1].split(',')
        hex_list = rgb_to_hex(rgb_vals)
        hex_string = ''.join(hex_list)
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

# Part 2 - Select Colour

def select_color():
    print('Enter the RGB values of your colour.')

    r = input('R: ')
    g = input('G: ')
    b = input('B: ')

    rgb = (r, g, b)

    if rgb in colour_dictionary:
        print('Colour ' + str([r, g, b]) + ' is ' + colour_dictionary[rgb][0] + ' and has hex code ' + colour_dictionary[rgb][1])
    else:
        print('Colour ' + str([r, g, b]) + ' not found. Would you like to:')
        print('1. Enter a name for this colour')
        print('2. Return to the main menu')
        print('\n')

        user_input = input('Select an option: ')
        if user_input == '1':
            user_colour = input("What is the colour's name? ")
            hex_list = rgb_to_hex(list(rgb))
            hex_code = ''.join(hex_list)
            print('Colour ' + str([r, g, b]) + ' is ' + user_colour + ' and has hex code ' + hex_code)
            
            # Add user's custom colour to dictionary
            colour_dictionary[rgb] = [user_colour, hex_code]
        elif user_input == '2':
            return

# Part 3 - Finding the Closest Colour

def find_closest_colour():
    print('Enter the RGB values of your colour.')

    r = input('R: ')
    g = input('G: ')
    b = input('B: ')

    rgb = (r, g, b)

    if rgb in colour_dictionary:
        print('Colour ' + str([r, g, b]) + ' is ' + colour_dictionary[rgb][0] + ' and has hex code ' + colour_dictionary[rgb][1])
    else:
        # Find closest colour by calcuating absolute difference between all values
        min_val = 2 ** 31
        for key in colour_dictionary:
            red = int(key[0])
            green = int(key[1])
            blue = int(key[2])

            val = abs(red - int(r)) + abs(green - int(g)) + abs(blue - int(b))
            
            if val < min_val:
                min_val = val
                closest_colour = [str(red), str(green), str(blue)]

        print('\n')
        print('The closest colour to ' + str([r, g, b]) + ' is ' + str(closest_colour) + ', ' + colour_dictionary[tuple(closest_colour)][0] + ', with hex code ' + colour_dictionary[tuple(closest_colour)][1] + '.')
        print('The absolute difference between the two colours is ' + str(min_val) + '.')

def display_and_save_colour_scheme():
    print('Enter the RGB values of your base colour.')

    r = int(input('R: '))
    g = int(input('G: '))
    b = int(input('B: '))

    user_rgb_list = [r, g, b]

    print('Which colour scheme do you wish to display?')
    print('M: Monochrome')
    print('C: Complementary')

    user_colour_scheme_choice = input('Select an option: ').lower()

    # A colour square is a 240 x 240 image (list of list of pixels)

    lightest_pixels = lighten_pixel_colour(user_rgb_list, 0.8)
    slightly_lighter_pixels = lighten_pixel_colour(user_rgb_list, 0.5)

    slightly_darker_pixels = darken_pixel_colour(user_rgb_list, 0.5)
    darkest_pixels = darken_pixel_colour(user_rgb_list, 0.8)

    height = 240
    if user_colour_scheme_choice == 'm':
        width = 240
    else:
        width = 480
        complement_pixels = complement_pixel_colour(user_rgb_list)
        
        lightest_pixels_complement = lighten_pixel_colour(complement_pixels, 0.8)
        slightly_lighter_pixels_complement = lighten_pixel_colour(complement_pixels, 0.5)

        slightly_darker_pixels_complement = darken_pixel_colour(complement_pixels, 0.5)
        darkest_pixels_complement = darken_pixel_colour(complement_pixels, 0.8)

    canvas = cmpt120image.getBlackImage(width, height)

    if user_colour_scheme_choice == 'm':
        for row in range(height):
            for col in range(width):
                # Populate with lighter values
                if (row < 80) and (col >= 0 and col < 80):
                    canvas[row][col] = lightest_pixels
                elif row < 80 and col >= 160:
                    canvas[row][col] = slightly_lighter_pixels
                # Form cross
                elif (row >= 80 and row < 160) or (col >= 80 and col < 160):
                    canvas[row][col] = user_rgb_list
                # Populate with darker values
                elif (row >= 160) and (col >= 0 and col < 80):
                    canvas[row][col] = slightly_darker_pixels
                elif row >= 160 and col >= 160:
                    canvas[row][col] = darkest_pixels
    else:
        for row in range(height):
            for col in range(width):
                # Populate with lighter values
                if (row < 80) and (col >= 0 and col < 80):
                    canvas[row][col] = lightest_pixels
                elif (row < 80) and (col >= 160 and col < 240):
                    canvas[row][col] = slightly_lighter_pixels
                elif (row < 80) and (col >= 240 and col < 320):
                    canvas[row][col] = lightest_pixels_complement
                elif (row < 80) and (col >= 400):
                    canvas[row][col] = slightly_lighter_pixels_complement

                # Populate with original and complement values
                elif (row < 80) and (col >= 80 and col < 160):
                    canvas[row][col] = user_rgb_list
                elif (row < 80) and (col >= 320 and col < 400):
                    canvas[row][col] = complement_pixels
                elif (row >= 80 and row < 160) and (col < 240):
                    canvas[row][col] = user_rgb_list
                elif (row >= 80 and row < 160) and (col >= 240):
                    canvas[row][col] = complement_pixels
                elif (row >= 160) and (col >= 80 and col < 160):
                    canvas[row][col] = user_rgb_list
                elif (row >= 160) and (col >= 320 and col < 400):
                    canvas[row][col] = complement_pixels

                # Populate with darker values
                elif (row >= 160) and (col >= 0 and col < 80):
                    canvas[row][col] = slightly_darker_pixels
                elif (row >= 160) and (col >= 160 and col < 240):
                    canvas[row][col] = darkest_pixels
                elif (row >= 160) and (col >= 240 and col < 320):
                    canvas[row][col] = slightly_darker_pixels_complement
                elif (row >= 160) and (col >= 400):
                    canvas[row][col] = darkest_pixels_complement

    cmpt120image.showImage(canvas)
    cmpt120image.saveImage(canvas, 'cscheme.png')

main()

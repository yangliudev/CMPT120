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

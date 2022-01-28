def dark_side():

    print('I will decide if you can join the Dark Side.')

    color = input('Is red your favorite color? ').lower()
    cape = input('Do you like capes? ').lower()

    if color == 'yes' or cape == 'yes':
        print('Dark side it is!')
    else:
        print('Light side, I see.')

dark_side()
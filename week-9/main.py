# Yang Liu
# CMPT 120 D400
# March 16, 2022

import cmpt120image
import cmpt120imageManip
import pathlib

def main():
    img = cmpt120image.getImage(str(pathlib.Path(__file__).parent.resolve()) + '/bird.png')

    print('FILTERS')
    print('1: Swap red and green')
    print('2: Convert to black and white')
    print('3: Reflect')
    print('4: Brighten')
    print('5: Reload Image')
    print('0: Quit')

    while True:
        num = input('Enter 1 to 5, 0 to quit: ')
        if num == '0':
            return
        elif num == '1':
            cmpt120imageManip.swapRedGreen(img)
        elif num == '2':
            cmpt120imageManip.blackWhite(img)
        elif num == '3':
            cmpt120imageManip.reflect(img)
        elif num == '4':
            cmpt120imageManip.brighten(img)
        elif num == '5':
            img = cmpt120image.getImage(str(pathlib.Path(__file__).parent.resolve()) + '/bird.png')
            cmpt120image.showImage(img)
    
main()

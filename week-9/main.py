import cmpt120image
import pathlib

def main():
    img = cmpt120image.getImage(str(pathlib.Path(__file__).parent.resolve()) + '/bird.png')
    print(img)

main()

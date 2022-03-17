import cmpt120image
import cmpt120imageManip
import pathlib

def main():
    img = cmpt120image.getImage(str(pathlib.Path(__file__).parent.resolve()) + '/bird.png')

    cmpt120imageManip.blackWhite(img)
    cmpt120imageManip.swapRedGreen(img)
    cmpt120imageManip.reflect(img)
    
main()

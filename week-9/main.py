import cmpt120image
import cmpt120imageManip

import pathlib
import subprocess

def main():
    img = cmpt120image.getImage(str(pathlib.Path(__file__).parent.resolve()) + '/bird.png')

    cmpt120imageManip.blackWhite(img)

    # Copy output to clipboard
    # subprocess.run("pbcopy", universal_newlines=True, input=str(img))
    
main()

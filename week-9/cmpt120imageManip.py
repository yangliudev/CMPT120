import cmpt120image

def blackWhite(img):
    height = len(img)
    width = len(img[0])

    canvas = cmpt120image.getBlackImage(width, height)

    for row in range(height):
        for col in range(width):
            ls = img[row][col]
            if sum(ls) < 384:
                # Change to black
                canvas[row][col] = [0, 0, 0]
            else:
                # Change to white
                canvas[row][col] = [255, 255, 255]

    cmpt120image.saveImage(canvas, 'test.png')
    
import cmpt120image

def swapRedGreen(img):
    height = len(img)
    width = len(img[0])

    canvas = cmpt120image.getBlackImage(width, height)

    for row in range(height):
        for col in range(width):
            r = img[row][col][0]
            g = img[row][col][1]
            b = img[row][col][2]

            # Red and green swap places, blue stays in place
            canvas[row][col] = [g, r, b]

    cmpt120image.saveImage(canvas, 'imgRGswap.png')

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

    cmpt120image.saveImage(canvas, 'imgBW.png')

def reflect(img):
    height = len(img)
    width = len(img[0])

    canvas = cmpt120image.getBlackImage(width, height)

    # We only want the top half of the image
    ls = img[0]
    len_half_ls = len(ls) // 2
    top_half = ls[:len_half_ls]
    print(top_half)

    joined = top_half + top_half

    cmpt120image.saveImage([joined], 'imgReflect.png')

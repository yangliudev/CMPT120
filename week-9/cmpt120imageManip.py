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

    for row in range(height // 2):
        for col in range(width):
            canvas[row][col] = img[row][col]

    reflected_canvas = canvas[::-1]

    for row in range(height // 2, height):
        for col in range(width):
            canvas[row][col] = reflected_canvas[row][col]

    cmpt120image.saveImage(canvas, 'imgReflect.png')

"""
    Original

    [ 
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]

    Reflection would be

    [ 
        [1, 2, 3],
        [4, 5, 6],
        [4, 5, 6],
        [1, 2, 3]
    ]
"""

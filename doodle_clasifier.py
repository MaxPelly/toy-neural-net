import numpy as np
from PIL import Image
from matricies import Matrix

def to_image(data):
    x_size = 28
    y_size = 28

    im = Image.new('L', (x_size, y_size))
    pix = im.load()

    for y in range(x_size):
        for x in range(y_size):
            i = y * y_size + x
            pix[x,y] = int(data[i])

    im.show()
    return im

TRAIN = Matrix.from_array((1, 0, 0))
RAINBOW = Matrix.from_array((0, 1, 0))
CAT = Matrix.from_array((0,0,1))


trains = np.load('doodles/train1000.npy')
rainbows = np.load('doodles/rainbow1000.npy')
cats = np.load('doodles/cat1000.npy')

to_image(cats[23])



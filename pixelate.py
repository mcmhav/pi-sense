from sense_hat import SenseHat
from PIL import Image
import math
import picamera

camera = picamera.PiCamera()
camera.capture('image.jpg')

pixels = 8
backgroundColor = (0,)*3
pixelSize = 100

image = Image.open('image.jpg')

image_width = image.size[0]
image_height = image.size[1]

size_diff = image_width - image_height

width_reduction = 0
height_reduction = 0

new_width_min = 0
new_width_max = image_width
new_height_min = 0
new_height_max = image_height
if size_diff > 0:
    new_width_min = math.fabs(size_diff) / 2
    new_width_max = image_width - math.fabs(size_diff) / 2
elif size_diff < 0:
    new_height_min = math.fabs(size_diff) / 2
    new_height_max = image_height - math.fabs(size_diff) / 2

image = image.crop(
    (
        new_width_min,
        new_height_min,
        new_width_max,
        new_height_max
    )
)

pixelSize = math.floor(image.size[0]/pixels)

image = image.resize(
    (
        math.floor(image.size[0]/pixelSize),
        math.floor(image.size[1]/pixelSize)
    ),
    Image.NEAREST
)
image = image.resize(
    (
      math.floor(image.size[0]*pixelSize),
      math.floor(image.size[1]*pixelSize)
    ),
    Image.NEAREST
)

maxsize = (pixels, pixels)
image.thumbnail(maxsize, Image.NEAREST)
image.save('output.jpg')

sense = SenseHat()

# sense.set_pixel(2, 2, (0, 0, 255))
# sense.set_pixel(4, 2, (0, 0, 255))
# sense.set_pixel(3, 4, (100, 0, 0))
# sense.set_pixel(1, 5, (255, 0, 0))
# sense.set_pixel(2, 6, (255, 0, 0))
# sense.set_pixel(3, 6, (255, 0, 0))
# sense.set_pixel(4, 6, (255, 0, 0))
# sense.set_pixel(5, 5, (255, 0, 0))


def test():
    pixel = image.load()
    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            sense.set_pixel(i, j, pixel[i, j])

            print(pixel[i, j])
            print(pixel[i, j])


test()


def border():
    pixel = image.load()

    for i in range(0, image.size[0], pixelSize):
        for j in range(0, image.size[1], pixelSize):
            for r in range(pixelSize):
                pixel[i+r, j] = backgroundColor
                pixel[i, j+r] = backgroundColor

# image.save('output.jpg')

from PIL import Image
import math
from sense_hat import SenseHat
from time import sleep
import picamera

IMAGE_LOCATION = 'image.jpg'


def take_picture():
    camera = picamera.PiCamera()
    camera.capture(IMAGE_LOCATION)


def convert_image_to_pixels():
    pixels = 8
    pixel_size = 100

    image = Image.open(IMAGE_LOCATION)

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
        new_width_min = int(math.fabs(size_diff) / 2)
        new_width_max = int(image_width - math.fabs(size_diff) / 2)
    elif size_diff < 0:
        new_height_min = int(math.fabs(size_diff) / 2)
        new_height_max = int(image_height - math.fabs(size_diff) / 2)

    image = image.crop(
        (
            new_width_min,
            new_height_min,
            new_width_max,
            new_height_max
        )
    )

    pixel_size = math.floor(image.size[0]/pixels)

    # print(int(math.floor(image.size[0]/pixel_size)))
    # print(int(math.floor(image.size[1]/pixel_size)))
    # print(Image.NEAREST)

    # image = image.resize(
    #     (
    #         int(math.floor(image.size[0]/pixel_size)),
    #         int(math.floor(image.size[1]/pixel_size))
    #     ),
    #     Image.NEAREST
    # )
    # image = image.resize(
    #     (
    #       int(math.floor(image.size[0]*pixel_size)),
    #       int(math.floor(image.size[1]*pixel_size))
    #     ),
    #     Image.NEAREST
    # )

    print('==============')
    print(pixels)
    print(Image.NEAREST)
    print('==============')

    maxsize = (pixels, pixels)
    image.thumbnail(maxsize, Image.NEAREST)
    image.save('output.jpg')

    return image, pixel_size


def pixelate():
    take_picture()

    image, pixel_size = convert_image_to_pixels()

    sense = SenseHat()

    def test():
        pixel = image.load()
        for i in range(0, image.size[0]):
            for j in range(0, image.size[1]):
                sense.set_pixel(i, j, pixel[i, j])

                print(pixel[i, j])
                print(pixel[i, j])

    test()

    sleep(10)

    sense.clear()

    def border():
        background_color = (0,)*3
        pixel = image.load()

        for i in range(0, image.size[0], pixel_size):
            for j in range(0, image.size[1], pixel_size):
                for r in range(pixel_size):
                    pixel[i+r, j] = background_color
                    pixel[i, j+r] = background_color

    # image.save('output.jpg')


pixelate()

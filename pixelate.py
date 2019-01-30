from PIL import Image
import math
from sense_hat import SenseHat
from time import sleep
import picamera
import time

IMAGE_LOCATION = 'image.jpg'


def take_picture():
    # camera = picamera.PiCamera()
    # camera.capture(IMAGE_LOCATION)

    # with picamera.PiCamera() as camera:
    #     camera.start_preview()
    #     # camera.exposure_compensation = 2
    #     # camera.exposure_mode = 'spotlight'
    #     # camera.meter_mode = 'matrix'
    #     # camera.image_effect = 'gpen'
    #     # time.sleep(2)
    #     camera.capture(IMAGE_LOCATION)
    #     camera.stop_preview()

    camera = picamera.PiCamera()
    try:
        # camera.start_preview()
        camera.capture(IMAGE_LOCATION)
        # camera.stop_preview()
    finally:
        camera.close()


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


def pixelate(sense):

    image, pixel_size = convert_image_to_pixels()

    def test():
        pixel = image.load()
        for i in range(0, image.size[0]):
            for j in range(0, image.size[1]):
                sense.set_pixel(i, j, pixel[i, j])

                print(pixel[i, j])
                print(pixel[i, j])

    test()

    sleep(5)

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


SENSE = SenseHat()

while True:
    for event in SENSE.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            take_picture()

            pixelate(SENSE)

            # Check which direction
            # if event.direction == "up":
            #     sense.show_letter("U")      # Up arrow
            # elif event.direction == "down":
            #     sense.show_letter("D")      # Down arrow
            # elif event.direction == "left":
            #     sense.show_letter("L")      # Left arrow
            # elif event.direction == "right":
            #     sense.show_letter("R")      # Right arrow
            # elif event.direction == "middle":
            #     sense.show_letter("M")      # Enter key

            # Wait a while and then clear the screen
            sleep(10)
            SENSE.clear()

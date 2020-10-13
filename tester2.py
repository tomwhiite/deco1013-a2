from microbit import *
from gesture import *
import neopixel
import random
from random import randint

gesture = Gesture()
display.show(Image.YES)
sleep(500)
np = neopixel.NeoPixel(pin1, 60)
display.clear()

while True:

    for pixel_id in range(0, len(np)):
        red = randint(0, 60)
        green = randint(0, 60)
        blue = randint(0, 60)

    g = gesture.read()
    if g == 'up':
        np.show()
        print(g)
    elif g == 'down':
        np.clear()
        print(g)

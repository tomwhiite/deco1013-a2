from microbit import *
from gesture import *
import music
import neopixel

gesture = Gesture()

counter = 1

# set colours:
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (0, 255, 255)
colour = [red, green, blue, yellow, cyan, magenta]


clockwise = Image("99999:"
                  "00009:"
                  "09009:"
                  "99990:"
                  "09000:")
anticlockwise = Image("99999:"
                      "90000:"
                      "90090:"
                      "09999:"
                      "00090:")
forward = Image("09090:"
                "99099:"
                "00000:"
                "99099:"
                "09090:")
backward = Image("99099:"
                 "90009:"
                 "00000:"
                 "90009:"
                 "99099:")
wave = Image("00090:"
			 "99999:"
			 "00000:"
			 "99999:"
			 "09000:")

gesture_map = {
    'up': Image.ARROW_N,
    'down': Image.ARROW_S,
    'left': Image.ARROW_W,
    'right': Image.ARROW_E,
    'forward': forward,
    'backward': backward,
    'clockwise': clockwise,
    'anticlockwise': anticlockwise,
    'wave': wave
}

display.show(Image.YES)
sleep(500)

while True:

    np = neopixel.NeoPixel(pin3, counter)
    for i in range(0, len(np)):
        np[i] = (255, 0, 255)
        np.show()
        sleep(500)

    g = gesture.read()
    if g == 'none':
        display.clear()
    else:
        print(g)
        display.show(gesture_map[g])
        sleep(300)

    if g == 'up':
        music.play(music.POWER_UP)
        np.show()
    elif g == 'down':
        music.play(music.POWER_DOWN)
        np.clear()


display.show(Image.GIRAFFE)

import time
import RPi.GPIO as GPIO
from tilehandle import TileState

tile = TileState()

GPIO.setmode(GPIO.BCM)

def motion(padPin):
    tile.tile_handle(padPin)

pins= [24,27, 13, 15]
for pin in pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin, GPIO.RISING, callback=motion)

pad_already_pressed = False

try: 
    time.sleep(1)
    while 1:  
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()



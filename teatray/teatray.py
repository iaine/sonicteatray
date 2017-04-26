import time
import RPi.GPIO as GPIO
from tilehandle import TileState

tile = TileState()

GPIO.setmode(GPIO.BCM)

#import pygame.mixer

#pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

#initialise sounds
#print "played"
#cuckoo = pygame.mixer.Sound("home/iain/fail.wav")

# initialise buttons
#padPin = 24
#GPIO.setup(padPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#padPin2 = 27
#GPIO.setup(padPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
pins= [24,27]
for pin in pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin, GPIO.RISING, callback=motion)

pad_already_pressed = False
#pad_already_pressed_2 = False

def motion(padPin):
    tile.handle(padPin)
#    global pad_already_pressed
#    if not pad_already_pressed:
#        pygame.mixer.music.load("/home/iain/wheatear.mp3") 
#        pygame.mixer.music.play()
#        print "Motion detected on " + str(padPin)
#        pad_already_pressed = True


#def stopmotion(padPin):
#    global pad_already_pressed_2
#    if not pad_already_pressed_2:
#        pygame.mixer.music.load("/home/iain/cuckoo.mp3")
#        pygame.mixer.music.play()
#        print "Stop Motion detected on " + str(padPin)
#        pad_already_pressed_2 = True

GPIO.add_event_detect(padPin, GPIO.RISING, callback=motion)
#GPIO.add_event_detect(padPin2, GPIO.RISING, callback=stopmotion)

try: 
    time.sleep(1)
    
    while 1:  
        time.sleep(1)
        
        pad_already_pressed = False
        pad_already_pressed_2 = False
except KeyboardInterrupt:
    GPIO.cleanup()
#pause()



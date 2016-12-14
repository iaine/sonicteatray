#from gpiozero import Button
#from signal import pause
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import pygame.mixer
#from pygame.mixer import Sound
#initialise mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

#initialise sounds
print "played"
cuckoo = pygame.mixer.Sound("home/iain/fail.wav")

# initialise buttons
padPin = 24
GPIO.setup(padPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

padPin2 = 27
GPIO.setup(padPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


pad_already_pressed = False
pad_already_pressed_2 = False

def motion(padPin):
    global pad_already_pressed
    if not pad_already_pressed:
        pygame.mixer.music.load("/home/iain/wheatear.mp3") 
        pygame.mixer.music.play()
        print "Motion detected on " + str(padPin)
        pad_already_pressed = True


def stopmotion(padPin):
    global pad_already_pressed_2
    if not pad_already_pressed_2:
        pygame.mixer.music.load("/home/iain/cuckoo.mp3")
        pygame.mixer.music.play()
        print "Stop Motion detected on " + str(padPin)
        pad_already_pressed_2 = True

GPIO.add_event_detect(padPin, GPIO.RISING, callback=motion)
GPIO.add_event_detect(padPin2, GPIO.RISING, callback=stopmotion)
#while 1:
    #button.when_pressed = tweeter.play
try: 
    time.sleep(1)
    print ("Ready for some pins")
    #while 1:
    #    if GPIO.input(padPin) and not pad_already_pressed:
    #        print "Some motion"
        #    tweeter.play
            #pad_already_pressed = True

        #if not GPIO.input(padPin2) and not pad_already_pressed_2:
        #    print "Other motion"
        #    pad_already_pressed_2 = True
    while 1:  
        time.sleep(1)
        print("resetting")
        pad_already_pressed = False
        pad_already_pressed_2 = False
except KeyboardInterrupt:
    GPIO.cleanup()
#pause()



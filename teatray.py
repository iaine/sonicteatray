import pygame

from time import time

#paused state
is_paused = False
#the position of the track
current_position = 0.0
current_time  = None

def play(filename):
    '''
       Start to play a file
    '''

    pygame.init()
    pygame.mixer.init()
    #have to load the file name
    pygame.mixer.music.load(filename)
    #pygame.mixer.music.volume(0.5)
    pygame.mixer.music.play(start=current_position)

def stop():
    '''
       Stop the audio
    '''
    pygame.mixer.music.stop()

def pause(current_time):
    '''
      Pause the file as we've moved away
    '''
    pygame.mixer.music.pause()
    current_position = pygame.mixer.music.get_pos()
    #grab the current time
    print str(time())
    current_time = time()

if __name__ == "__main__":

    play("DragonBite.wav")
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)

    play("DragonBite.wav")
    pause(current_time)
    print current_time

import pygame

from time import time


class Audio():
    def __init__(self):
        #paused state
        self.is_paused = False
        #the position of the track
        self.current_position = 0.0
        self.current_time  = None

    def play(self, filename):
        '''
           Start to play a file
        '''

        pygame.init()
        pygame.mixer.init()
        #have to load the file name
        pygame.mixer.music.load(filename)
        #pygame.mixer.music.volume(0.5)
        pygame.mixer.music.play(start=self.current_position)

    def stop(self):
        '''
           Stop the audio
        '''
        pygame.mixer.music.stop()

    def pause(self):
        '''
           Pause the file as we've moved away
        '''
        pygame.mixer.music.pause()
        self.current_position = pygame.mixer.music.get_pos()
        #grab the current time
        self.current_time = time()

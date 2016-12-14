'''
   Audio handling
'''

import pygame.mixer

class Audio():
    
    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

    def play(self, filename):
        '''
           Play a file. 
        '''
        if filename is None or filename == '':
            print("It fewll over")
        else:
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play() 
            while pygame.mixer.get_busy():
                pygame.time.delay(100)

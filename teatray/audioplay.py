'''
   Audio handling
'''

import pygame.mixer

class Audio():

    def __init__(self):
        self.set_time = None
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

    def play(self, filename):
        '''
           Play a file. 
        '''
        if filename is None or filename == '':
            print("It fewll over")
        else:
            try:
                if not pygame.mixer.music.load(filename):
                    raise Exception ("file not foud")
                pygame.mixer.music.play()    
                while pygame.mixer.music.get_busy():
                    pygame.time.delay(100)
            except Exception, e:
                print(e)

    def pause(self):
        '''
           Pause the file and set the position if we need to return
        '''
        pygame.mixer.music.pause()
        self.set_time = pygame.mixer.music.get_pos()
        

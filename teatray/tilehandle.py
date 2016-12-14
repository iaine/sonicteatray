'''
   Handle the tile and mappings
'''

class TileState():
    state = None

    def __init__(self):
        self.state = False

    def handle_tile(self, tile_num):
        '''
           Handles the sensor and audio interface
        '''
        #change the state
        self.state = True

        #return the type of MP3 by the tile
        if tile_num is 25:
            return "wheatear.mp3"

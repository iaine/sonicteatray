'''
   Handle the tile and mappings
'''
from dao import DAO
from datetime import datetime

class TileState():
    state = None
    overview = None
    cmd_time = 0

    def __init__(self):
        self.state = False
        self.overview = False
        self.cmd_time = 0

    def handle_tile(self, tile_num):
        '''
           Handles the sensor and audio interface
        '''
        #change the state
        self.state = True
        if tile_num == 30: 
            self.overview = True
            self.cmd_time = datetime.now()

        #return the type of MP3 by the tile
        return self._get_file_for_tile(tile_num)

    def _get_file_for_tile (self, tile_num):
        '''
           Interface for fetching the file attached to the tile
        '''
        #return the type of MP3 by the tile
        try:
            if tile_num is None:
                raise Exception("No tile given")

            db = DAO()
            fname = db.fetch(tile_num)

            if fname is None:
                raise Exception("No file returned")
            else:
                return fname
        except Exception,e:
            print(e)

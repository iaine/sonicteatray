'''
   Data Access file
'''
import sqlite3

class DAO():

    def __init__(self):
        conn = sqlite3.connect('teatraystore.db')
        self.db = conn.cursor()

    def check_table_exists(self, table_name):
        '''
          Query to check thatthe table exists. If not create it.
          @parameter: table_name - the table name for query
        '''
        self.db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        if self.db.fetchone() is None:
            self.db.execute(''' CREATE TABLE sounds
                                (tile_num real, soundfile text)''')

    def fetch(self, tile):
        '''
          Fetch the sound file linked to the tile number
          @parameter tile, integer for the tile number
        '''

        try:
            self.db.execute('SELECT soundfile FROM sounds WHERE tile_num=?', (tile,))
            return self.db.fetchone()[0]
        except Exception,e:
            print (e)

    def insert_data(self, data):
        '''
          Method to insert data
        '''
        self.db.executemany("INSERT INTO sounds VALUES (?,?)", data)

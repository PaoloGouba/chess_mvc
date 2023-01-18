from players import Player
from matches import Match
class Tourn():
    def __init__(self, name : str,start_time='',end_time=''):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        return
    
    def get_match_list(self):
        return match_list
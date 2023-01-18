from players import Player
from matches import Match
class Tourn():
    def __init__(self, name : str, start_time : str, end_time : str):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        return
    
    @classmethod
    def create_tourn(self, name : str, start_time : str, end_time : str):
        
        tourn = Tourn(name,start_time)
        
        return tourn
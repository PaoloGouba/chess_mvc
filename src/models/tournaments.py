from players import Player

TOURNEMENT_GAMES_NB = 4


class Tournament():
    """
    Tournament model        
    """
    def __init__(self, name : str, location : str, date : tuple, timestamp : str, description : str ):
        """
        __ini__ : 
            Definition of Tournament attributes        
        
        """
        self.name = name
        self.location = location
        self.date = date
        self.timestamp = timestamp
        self.description = description
        
        return
    
    # get players for tournament
    def load_players(self):
        
        players = []
        
        player1 = Player()
        
        return players
    
    def generate_tourns(self,players):
        pass
    

    

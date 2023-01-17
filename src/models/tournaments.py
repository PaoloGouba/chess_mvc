TOURNEMENT_GAMES_NB = 4


class Tournament():
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
        pass
    
    def generate_games_list(self):
        pass
    

    

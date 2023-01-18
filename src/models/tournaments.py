from players import Player
#import tools.commons as t
import datetime

TOURNEMENT_GAMES_NB = 4
PLAYERS_NB = 7


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
        
        for player in PLAYERS_NB :
            player = Player.create_player()
            players.append(player)

        return players
    
    def create_tourns(self):
        return tourns
    
    @classmethod
    def create_tournament(self, name : str, location : str,timestamp : str,description  : str = ''):
        
        current_time = datetime.datetime.now()
        date = (current_time,)
        new_tournament = Tournament(name, location, date, timestamp,description)
        
        return new_tournament



my_new_tournament = Tournament.create_tournament('Tournoi 1','Paris','Timestamp')
print(my_new_tournament.date)


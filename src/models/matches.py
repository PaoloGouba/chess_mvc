from players import Player

class Match():
    def __init__(self, match_players : tuple):
        
        self.match_players = match_players
        
        return
    
    @classmethod
    def create_match(self,player_1 : Player, player_2 : Player):
        
        match_player_1 = (player_1,player_1.rank)
        match_player_2 = (player_2,player_2.rank)
        
        return (match_player_1,match_player_2)
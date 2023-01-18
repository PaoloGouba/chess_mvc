class Player():
    """
    Player Model according to th e documentation
    """   
    
    def __init__(self, player_id : int, name : str, surname : str, gender : str, rank_pos : int , birthday : str):
        """
        __ini__ : 
            Definition of Player attributes        
        
        """
        self.player_id = player_id
        # self.player_id = id ? 
        self.name = name
        self.surname = surname
        self.gender = gender 
        self.rank = rank_pos
        self.birthday = birthday
        
        return
    
    
    def create_player(self,player_id, name, surname, gender, birthday, rank_pos=0):
        
        player = Player(player_id, name, surname, gender, birthday,rank_pos,)
        
        return player
class Player():
    """
    Player Model according to th e documentation
    """   
    
    def __init__(self, name : str, surname : str, gender : str, rank_pos : int > 0, birthday : str):
        """
        __ini__ : 
            Definition of Player attributes        
        
        """
        self.name = name
        self.surname = surname
        self.gender = gender 
        self.rank = rank_pos
        self.birthday = birthday
        
        return
    
    
    
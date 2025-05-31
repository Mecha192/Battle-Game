from enemies import enemy

class fairy(enemy):
    def __init__(self):
        super().__init__("Fairy", 15)
        self.attack = 10
        self.defense = 0
        self.speed = 20
        buff = {"melee" : "immune"}
        debuff = {"magic" : 2}

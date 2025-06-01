from enemies import enemy

class fairy(enemy):
    def __init__(self):
        super().__init__("Fairy", 15, 10, 0, 20)
        self.buff = {"melee" : "immune"}
        self.debuff = {"magic" : 2}

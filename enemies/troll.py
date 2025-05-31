from enemies import enemy

class troll(enemy):
    def __init__(self):
        super().__init__("Troll", 100)
        self.attack = 25
        self.defense = 15
        self.speed = 5

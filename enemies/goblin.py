from enemies import enemy

class goblin(enemy):
    def __init__(self):
        super().__init__("Goblin", 25)
        self.attack = 10
        self.defense = 5
        self.speed = 15

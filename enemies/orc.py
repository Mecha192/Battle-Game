from enemies import enemy

class orc(enemy):
    def __init__(self):
        super().__init__("Orc", 60)
        self.attack = 15
        self.defense = 10
        self.speed = 10

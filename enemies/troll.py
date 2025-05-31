from enemies import enemy

class troll(enemy):
    def __init__(self):
        super().__init__("Troll", 100)
        self.attack = 20
        self.defense = 15
        self.speed = 5

    def regen(self):
        self.health += 10
        if self.health > 100:
            self.health = 100
        return self.health
    
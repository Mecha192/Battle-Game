from enemies import enemy

class goblin(enemy):
    def __init__(self):
        super().__init__("Goblin", 25, 5, 5, 15)

from enemies import enemy

class orc(enemy):
    def __init__(self):
        super().__init__("Orc", 60, 15, 10, 10)

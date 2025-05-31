class enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        target.health -= self.attack - target.defense

    def is_hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            return "Kill!"
        return self.health

    def __str__(self):
        return f"{self.name}: (Health: {self.health}, Attack Power: {self.attack}, Defense: {self.defense}, Speed: {self.speed})"

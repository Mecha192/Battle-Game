from player import *
from fairy import *
from goblin import *
from orc import *
from troll import *

class enemy:
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def attack(self, target):
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0
        target.is_hit(0, damage)

    def is_hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            return "Kill!"
        return self.health

    def __str__(self):
        print(f"{self.name}:")
        print(f"Base: (Health: {self.health}, Attack Power: {self.attack}, Defense: {self.defense}, Speed: {self.speed})")
        return f"With Modifiers: (Health: {self.health}, Attack Power: {self.attack}, Defense: {self.defense}, Speed: {self.speed})"

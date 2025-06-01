import pygame
from equipment import player_equipment
from battle import temp_modifiers, round
from enemies import *
from modifiers import player_modifiers

class player:
    def __init__(self, name, health=50, attack=10, defense=10, speed=10):
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
            return "You Lose"
        return self.health

    def player_inputs():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ENTER] == True:
            round += 1

    def player_equipment_mods(equipment=player_equipment):
        equipment_mods = {
            "weapons": equipment["weapons"].get_modifiers(),
            "armor": equipment["armor"].get_modifiers(),
            "accessories": equipment["accessories"].get_modifiers()
        }
        return equipment_mods

    def player_stats():
        player_equipment_stats = player_equipment_mods()

    def __str__(self):
        print(f"{self.name}:")
        print(f"Base: (Health: {self.health}, Attack Power: {self.attack}, Defense: {self.defense}, Speed: {self.speed})")
        return f"With Modifiers: (Health: {self.health}, Attack Power: {self.attack}, Defense: {self.defense}, Speed: {self.speed})"
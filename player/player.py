import pygame
from equipment import player_equipment
from battle import temp_modifiers, round
from modifiers import player_modifiers

class player:
    def __init__(self, name, health=50, attack=10, defense=10, speed=10):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

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

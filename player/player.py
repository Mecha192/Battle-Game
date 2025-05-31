import pygame
from equipment import player_equipment
from battle import temp_modifiers
from modifiers import player_modifiers

round = 0

def player_inputs():
    round_counter = round
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ENTER] == True:
        round_counter += 1

def player_equipment_mods(equipment=player_equipment):
    equipment_mods = {
        "weapons": equipment["weapons"].get_modifiers(),
        "armor": equipment["armor"].get_modifiers(),
        "accessories": equipment["accessories"].get_modifiers()
    }
    return equipment_mods

def player_stats():
    player_equipment_stats = player_equipment_mods()

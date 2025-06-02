from weapon import equipped_weapons
from armor import equipped_armors
from acessories import equipped_accessories
player_equipment = {
    "weapons": equipped_weapons,
    "armor": equipped_armors,
    "acessories": equipped_accessories
}

def get_modifiers():
    modifiers = {
        "weapons": player_equipment["weapons"].get_damage(),
        "armor": player_equipment["armor"].get_defense(),
        "accessories": player_equipment["acessories"].get_items()
    }
    return modifiers

def get_damage():
    total_damage = 0
    for weapon in player_equipment["weapons"]:
        total_damage += weapon.get("damage", 0)
    return total_damage

def get_defense():
    total_defense = 0
    for armor in player_equipment["armor"]:
        total_defense += armor.get("defense", 0)
    return total_defense

def get_items():
    return equipped_accessories

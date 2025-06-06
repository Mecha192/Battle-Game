def weapons():
    return {
        "dagger": {
            "name": "Dagger",
            "damage": 6,
            "type": "melee"
        },
        "throwing_knife": {
            "name": "Throwing Knife",
            "damage": 4,
            "type": "ranged"
        },
        "sword": {
            "name": "Sword",
            "damage": 10,
            "type": "melee"
        },
        "bow": {
            "name": "Bow",
            "damage": 8,
            "type": "ranged"
        },
    }

equipped_weapons = []

def equip_weapon(weapon_name):
    global equipped_weapons
    weapon = weapons().get(weapon_name)
    if weapon and weapon not in equipped_weapons:
        equipped_weapons.append(weapon)
        print(f"{weapon['name']} has been equipped.")
    else:
        print(f"{weapon_name} is not a valid weapon or is already equipped.")


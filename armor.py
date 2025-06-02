armors = {
    "helm": {
        "name": "Helmet",
        "defense": 3,
        "price": 60
    },
    "shoulders": {
        "name": "Shoulder Pads",
        "defense": 2,
        "price": 40
    },
    "chest": {
        "name": "Chestplate",
        "defense": 5,
        "price": 100
    },
    "hands": {
        "name": "Gauntlets",
        "defense": 2,
        "price": 20
    },
    "legs": {
        "name": "Leggings",
        "defense": 5,
        "price": 80
    },
    "boots": {
        "name": "Boots",
        "defense": 3,
        "price": 60
    }
}

equipped_armors = []

def equip_armor(armor_name):
    global equipped_armors
    armor = armors.get(armor_name)
    if armor and armor not in equipped_armors:
        equipped_armors.append(armor)
        print(f"{str.upper(armor['name'])} has been equipped.")
    else:
        if not armor:
            print(f"{str.upper(armor_name)} is not a valid armor.") 
        else:
            print(f"{str.upper(armor['name'])} is already equipped.")
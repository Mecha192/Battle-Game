def accessories():
    return {
            "necklace": {
                "name": "Necklace",
                "Buff: Speed Boost": 2
            },
            "bracelet": {
                "name": "Bracelet",
                "Buff: Attack Boost": 1
            },
            "ring_attack": {
                "name": "Attack Ring",
                "Buff: Attack Boost": 1
            },
            "ring_defense": {
                "name": "Defense Ring",
                "Buff: Defense Boost": 1
            },
            "belt": {
                "name": "Belt",
                "Buff: Defense Boost": 1
            },
    }
equipped_accessories = []

def equip_accessory(accessory_name):
    global equipped_accessories
    accessory = accessories().get(accessory_name)
    if accessory not in equipped_accessories:
        equipped_accessories.append(accessory)
        print(f"{accessory['name']} has been equipped.")
    else:
        print(f"{accessory_name} is not a valid acessory or is already equipped.")
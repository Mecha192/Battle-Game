from modifiers import *
def accessories():
    return {
            "necklace": {
                "name": "Necklace",
                "Speed Boost": 2
            },
            "bracelet": {
                "name": "Bracelet",
                "Attack Boost": 1
            },
            "ring_attack": {
                "name": "Attack Ring",
                "Attack Boost": 1
            },
            "ring_defense": {
                "name": "Defense Ring",
                "Defense Boost": 1
            },
            "belt": {
                "name": "Belt",
                "Defense Boost": 1
            },
    }
equipped_accessories = []

def equip_accessory(accessory_name):
    global equipped_accessories
    accessory = accessories().get(accessory_name)
    if accessory not in equipped_accessories:
        equipped_accessories.append(accessory)
        if "Attack Boost" in accessory:
            add_buff(accessory["Attack Boost"])
        if "Defense Boost" in accessory:
            add_buff(accessory["Defense Boost"])
        if "Speed Boost" in accessory:
            add_buff(accessory["Speed Boost"])
        print(f"{accessory['name']} has been equipped.")
    else:
        print(f"{accessory_name} is not a valid acessory or is already equipped.")

import player
import random

def room_empty():
    ran_event = 0
    random_event(ran_event)
    if ran_event == 0:
        print("The room is empty.")
    print("Rest? Y or N")
    choice = input().lower()
    if choice == 'y':
        print("You rest and regain your strength.")
        player.rest()
    elif choice == 'n':
        print("You decide to keep moving.")
    else:
        print("Invalid choice. Please enter Y or N.")
        room_empty()
    ran_event = 0
    return

def random_event(ran_event):
    events = [None, None, None, "You stumbled upon a shrine with an ancient artifact!"]
    number = random.randint(1, 10)
    event = None
    if number == 10:
        event = events[3]
        print(event)
    if "treasure" in event:
        print("You gain some gold!")
        player.add_gold(50)
    if "beast" in event:
        print("Prepare for battle!")
        # Here you would initiate a battle with a random enemy
    if "artifact" in event:
        print("You obsorb the power of the artifact.")
        player.add_max_health(10)
        ran_event = 1
    if event is None:
        return
    return ran_event
from enemies import enemy1, enemy2, enemy3

active_enemies = []
position1 = None
position2 = None
position3 = None
target = None
active_position = None

def enemy_active():
    if enemy1 is not None:
        active_enemies.append(enemy1)
    if enemy2 is not None:
        active_enemies.append(enemy2)
    if enemy3 is not None:
        active_enemies.append(enemy3)
    return enemy_position()

def enemy_position():
    for enemy in active_enemies:
        if position1 == None:
            position1 = enemy
        elif position2 == None:
            position2 = enemy
        elif position3 == None:
            position3 = enemy
        if position1 == None:
            return empty_room()
        return active_target()

def enemy_death():
    if target.health <= 0:
        active_position = None
        if active_position == None:
            if position1 is not None:
                active_target(position1)
            elif position2 is not None:
                active_target(position2)
            elif position3 is not None:
                active_target(position3)
            return
        
def active_target(position=position1):
    active_position = position
    target = active_position.getattr()
    
from enemies import enemy1, enemy2, enemy3

position1 = enemy1
position2 = enemy2
position3 = enemy3

def enemy_position():
    if position2 == None:
        position2 = enemy3
        position3 = None
    if position1 == None:
        position1 = enemy2
        position2 = None
    if position1 == None and position2 == None and position3 == None:
        return empty_room()
def selection():
buffs = {}
debuffs = {}
player_modifiers = [buffs, debuffs]

def add_buff(buff):
    buffs += buff
    return buffs

def add_debuff(debuff):
    debuffs += debuff
    return debuffs

def remove_buff(buff):
    if buff in buffs:
        buffs.remove(buff)
    return buffs

def remove_debuff(debuff):
    if debuff in debuffs:
        debuffs.remove(debuff)
    return debuffs
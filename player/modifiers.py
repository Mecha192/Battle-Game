from player import player_mod, round

buffs = {}
debuffs = {}
player_modifiers = [buffs, debuffs]

def add_buff(buff):
    global_buffs = buffs
    global_buffs += buff

def temp_buff(buff, rounds):
    global_buffs = buffs
    global_buffs += buff
    round_count = rounds
    if round_count == 0:
        global_buffs -= buff
        round_count = 0
    else:
        round_count -= 1

def add_debuff(debuff):
    global_debuffs = debuffs
    global_debuffs += debuff

def temp_debuff(debuff, rounds):
    global_debuffs = debuffs
    global_debuffs += debuff
    round_count = rounds
    if round_count == 0:
        global_debuffs -= debuff
        round_count = 0
    else:
        round_count -= 1
from player import *
from modslist import buffs_list, debuffs_list
from enemies import enemy

round = 0

def temp_modifiers():
    buffs = temp_buffs()
    debuffs = temp_debuffs()
    temp_modifiers = {
        "buffs": buffs,
        "debuffs": debuffs
    }
    return temp_modifiers

def temp_buffs(buffs):
    temp_b_mod = {
        "Attack": 0,
        "Defense": 0,
        "Speed": 0
    }
    for k,v in buffs:
        if k in buffs_list():
            if k == "Attack Boost":
                temp_b_mod["Attack"] += v
            if k == "Defense Boost":
                temp_b_mod["Defense"] += v
            if k == "Speed Boost":
                temp_b_mod["Speed"] += v
    return temp_b_mod

def temp_debuffs():
    debuffs = debuffs_list()
    temp_d_mod = {
        "Attack": 0,
        "Defense": 0,
        "Speed": 0
    }
    for k,v in debuffs:
        if k in debuffs_list():
            if k == "Attack Reduction":
                temp_d_mod["Attack"] += v
            if k == "Defense Reduction":
                temp_d_mod["Defense"] += v
            if k == "Speed Reduction":
                temp_d_mod["Speed"] += v
    return temp_d_mod

def temp_buff(buff, rounds):
    round_count = rounds
    if round_count == 0:
        global_buffs -= buff
        round_count = 0
    else:
        round_count -= 1

def temp_debuff(debuff, rounds):
    round_count = rounds
    if round_count == 0:
        global_debuffs -= debuff
        round_count = 0
    else:
        round_count -= 1
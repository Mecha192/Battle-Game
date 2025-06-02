import pygame
from equipment import player_equipment
import rooms
from battle import temp_modifiers, round
from enemies import *
from target import *
from modifiers import player_modifiers

class player:
    def __init__(self, name, health=50, attack=10, defense=10, speed=10):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.max_health = 50

    def rest(self, max_health):
        if self.health > max_health:
            return
        else:
            self.health = max_health
        return self.health
    
    def add_max_health(self, amount):
        if self.health == self.max_health:
            self.health += amount
            self.max_health += amount
        else:
            self.max_health += amount
        return self.max_health
    
    def attack(self, target):
        self.attack += player_equipment["weapons"].get_damage()
        self.attack += player_modifiers["Attack"]
        self.attack -= player_modifiers["Attack Reduction"]
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0
        target.is_hit(0, damage)
        if target.health <= 0:
            enemy_death(target)
            return f"You killed {target.name}!"
        return f"You attack {target.name}. You dealt {damage} damage."

    def is_hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            return "You Lose"
        return self.health

    def player_inputs():
        keys = pygame.key.get_pressed()
        target = player.get_target()
        if keys[pygame.K_c] == True:
            return self.__str__()
        if keys[pygame.K_e] == True:
            return target.__str__()
        if keys[pygame.K_ENTER] == True:
            round += 1

    def get_target():
        target_enemy = None
        return target_enemy
    
    def __str__(self):
        print(f"{self.name}:")
        print(f"Base: (Health: {self.health}, Attack Power: {self.attack}, Defense: {self.defense}, Speed: {self.speed})")
        return f"With Modifiers: (Health: {self.health}, Attack Power: {self.attack}, Defense: {self.defense}, Speed: {self.speed})"
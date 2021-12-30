from weapon import Weapon
from armor import Armor



class Player:
    def __init__(self, name:str, attack:int, health:int, defense:int):
        self.__name = name
        self.__attack = attack
        self.__health =  health
        self.__defense = defense
        self.__weapon = None
        self.__armor = None
    
        
        
        
    @property
    def defense(self):
        return self.__defense
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, health):
        self.__health = health
    
    @property
    def attack(self):
       return self.__attack
    
    @property
    def weapon(self):
        return self.__weapon
    @weapon.setter
    def weapon(self, weapon:Weapon):
        self.__weapon = weapon
        
    @property
    def armor(self):
        return self.__armor
    @armor.setter
    def armor(self, armor:Armor):
        self.__armor = armor
    
    
        
    
    
    
    
    
        
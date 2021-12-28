class Weapon:
    weapons_list = []
    def __init__(self, name:str, attack_bonus:int):
        self.__name = name
        self.__attack_bonus = attack_bonus
        
        Weapon.weapons_list.append(self)
        pass
    @property
    def name(self):
        return self.__name
    @property
    def attack_bonus(self):
        return self.__attack_bonus
    @attack_bonus.setter
    def attack_bonus(self, attack_bonus):
        self.__attack_bonus = attack_bonus
    pass
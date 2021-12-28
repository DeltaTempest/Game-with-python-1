class Armor:
    armors_list = []
    def __init__(self, name:str, defense_bonus:int):
        self.__name = name
        self.__defense_bonus = defense_bonus
        
        Armor.armors_list.append(self)
        pass
    @property
    def name(self):
        return self.__name
    @property
    def defense_bonus(self):
        return self.__attack_bonus
    @defense_bonus.setter
    def defense_bonus(self, attack_bonus):
        self.__attack_bonus = attack_bonus
    pass
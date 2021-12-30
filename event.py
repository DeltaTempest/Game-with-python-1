"""
Class Event adalah class yang mengisi cerita, terkait hal yang terjadi pada game dan mendisplaynya
"""
from armor import Armor
from player import Player
from textdisplay import TextDisplay
from weapon import Weapon


class Event(TextDisplay):
    def __init__(self,player_health:int, player_attack:int, player_weapon:Weapon, player_armor:Armor, player_name = "None"):
        self.__player_name = player_name
        self.__player_health = player_health
        self.__player_attack = player_attack
        self.__player_weapon = player_weapon
        self.__player_armor = player_armor
        self.__display_text = TextDisplay()
        pass
    
    
    
    def opening_event(self):
        print(self.display_text.on_opening_txt(self.player_name))
        while True:
            print(self.display_text.loop_on_opening_txt())
            number = int(input("Insert your number: "))
            print(f"\n{self.display_text.divided_lines}")
            if number == 1:
                self.first_story_explain()
                break
                
            elif number == 2:
                self.show_player_status()
                continue
                
            elif number == 3:
                pass
            else:
               
                continue
                pass
        
        pass
    
    def show_player_status(self):
        print(self.display_text.player_status_no_eq_txt(self.player_name, self.player_health, self.player_attack))
        pass
    def first_story_explain(self):
        pass
    def starting_game(self):
        print(self.display_text.starting_games_txt)
        while True:
            
            name = str(input("Insert name: "))
            if name == None or name == "":
                print(f"{self.__divided_lines()}\nPlease insert rigth name!\n{self.__divided_lines()}")
                continue
            else:
                return name
    @staticmethod
    def __divided_lines():
        return f"====================================="
    
    @property
    def player_name(self):
        return self.__player_name
    @player_name.setter
    def player_name(self, player_name):
        self.__player_name = player_name
    @property
    def player_health(self):
        return self.__player_health
    @property
    def player_attack(self):
        return self.__player_attack
    @property
    def player_weapon(self):
        return self.__player_weapon
    @property
    def player_armor(self):
        return self.__player_armor
    @property
    def display_text(self):
        return self.__display_text
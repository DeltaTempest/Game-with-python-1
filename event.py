"""
Class Event adalah class yang mengisi cerita, terkait hal yang terjadi pada game dan mendisplaynya
"""
from os import times_result
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
            word = str(input("Your answer: "))
            print(f"\n{self.display_text.divided_lines}")
            if word == "1":
                #show prologue story
                print(self.display_text.prolouge_story)
                break
                
            elif word == "2":
                #show player status
                self.show_player_status()
                continue
                
            elif word == "3":
                #begin the game
                
                pass
            elif word == "q" or word == "Q" or word == "Quit" or word == "quit":
                #quitting
                print(self.display_text.quiting_games_txt)
                return 0
            else:
                continue
                pass
        
        pass
    
    def show_player_status(self):
        while True:
            print(self.display_text.player_status_no_eq_txt(self.player_name, self.player_health, self.player_attack))
            print(f"{self.display_text.continue_or_not}\n")
            word = str(input("Input yes or no: "))
            print(self.display_text.divided_lines)
            if word == "yes" or word == "Yes":
                break
            elif word == "no" or word == "No":
                continue
            break
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
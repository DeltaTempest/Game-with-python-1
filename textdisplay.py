"""
class yang berfungsi mengkustomasi text untuk di tampilkan
"""

from typing import ClassVar
import math


class TextDisplay:
    
    def __init__(self):
        self.__divided_lines = f"""====================================="""
        self.__starting_games_txt = f"""{self.divided_lines}
Please insert your name to begin!
{self.__divided_lines}"""
        
        
    def on_opening_txt(self, player_name="none"):
        return f"""{self.divided_lines}
Welcome {player_name}!"""
    def loop_on_opening_txt(self):
        return f"""Please select one of these optionS!
1. See the story
2. See player status
3. Begin your adventure
{self.divided_lines}   
"""
    def player_status_no_eq_txt(self, player_name="none", player_health=0, player_attack=0):
        return f"""{self.divided_lines}
Name: {player_name}
Health: {player_health}
Attack Power: {player_attack} 
Weapon: None
Armor : None
{self.divided_lines}"""

    @property
    def divided_lines(self):
        return self.__divided_lines
    
    
    @property
    def starting_games_txt(self):
        return self.__starting_games_txt


text = TextDisplay()

# print(text.player_status_no_eq_txt("DeltaTempest", 10, 1))
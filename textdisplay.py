"""
class yang berfungsi mengkustomasi text untuk di tampilkan
"""





class TextDisplay:
    
    def __init__(self):
        self.__divided_lines = f"""====================================="""
        self.__starting_games_txt = f"""{self.divided_lines}
Please insert your name to continue!
{self.__divided_lines}"""

        self.__continue_or_not = f"""{self.divided_lines}
        
Continue?
[y/n]

{self.divided_lines}"""

        self.__quiting_games_txt = f"""{self.divided_lines}

Thanks for playing!

Quiting games...
        
{self.divided_lines}"""

        self.__proglouge_story = f"""
{self.divided_lines}{self.divided_lines}
        
Prolouge:

Once upon a time, a disaster struck a country. The disaster was caused by a monster called Amster. 
Luckily this monster was defeated, and finally the disaster that hit the country ended. 
Even if Amster was defeated, there was a price to pay after defeating the monster

{self.divided_lines}{self.divided_lines}"""
        
    
    def on_opening_txt(self, player_name="none"):
        return f"""{self.divided_lines}
    
Welcome {player_name}!"""
    def loop_on_opening_txt(self):
        return f"""
Please select one of these optionS!
1. See the story
2. See player status
3. Begin your adventure

Input 'q' to quit

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
    
    @property
    def continue_or_not(self):
        return self.__continue_or_not
    
    @property
    def quiting_games_txt(self):
        return self.__quiting_games_txt
    @property
    def prolouge_story(self):
        return self.__proglouge_story


text = TextDisplay()

# print(text.player_status_no_eq_txt("DeltaTempest", 10, 1))
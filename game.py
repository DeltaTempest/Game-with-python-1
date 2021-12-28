"""
Game class adalah class yang mengatur jalan cerita dan display dari text dalam game ini
"""
from player import Player
from weapon import Weapon
from armor import Armor

class Game:
    player = Player("None", 0, 10, 1)
    @classmethod
    def start(cls):
        fist = Weapon("Fist",1)
        
        
        while True:
            cls.__opening_event()
            
            break
    @classmethod
    def __opening_event(cls):
        print(f"""
{cls.__divided_lines()}
Welcome to rpg text games!""")
        
        while True:
            
            print(f"""Please select one of the option
1. The story
2. Status
3. Begin the journey
{cls.__divided_lines()}
""")
            
            num = int(input("Your number: "))
            if num == 1:
                cls.__the_story()
                continue
            elif num == 2:
            
                pass
            elif num == 3:
                return
                pass       
            else:
                
                print(f"""
{cls.__divided_lines()}
Please insert the right number!
{cls.__divided_lines()}
""")
                pass
    
    
    
    @staticmethod
    def __the_story():
        pass
        
    @staticmethod
    def __divided_lines():
        return f"====================================="   
"""
Game class adalah class yang mengatur jalan cerita dalam game ini
"""
from event import Event
from player import Player
from weapon import Weapon
from armor import Armor

class Game:
    new_player = None
    knife_weapon = None
    leather_armor = None
    new_event = None
    @classmethod
    def start(cls):
        cls.first_time_initialize() #menginisialisasi variabel class
        #menginisialisasi objek new_event 
        cls.new_event = Event(cls.new_player.health, cls.new_player.attack, cls.new_player.weapon, cls.new_player.armor)
        player_name = cls.new_event.starting_game() #menjalankan starting game function 
        cls.new_player.name = player_name #setting up nama player ke objek new_player
        cls.new_event.player_name = player_name #setting up nama player pada objek new_event 
        del player_name 
        
        num = cls.new_event.opening_event() #menjalankan opening event
        if num == 0:
            return
        del num
        
        
        
    @classmethod
    def first_time_initialize(cls):
        #initialize event
         
        #initialize player
        cls.new_player = Player("None", 1, 10, 0)
        """
        Player_attack = 1
        player_health = 10
        player_defense = 0
        player_weapon = None
        player_armor = None
        """
        #initialize enemy
        #initialize Weapon 
        cls.knife_weapon = Weapon("Knife", 2)
        #initialize armor
        cls.leather_armor = Armor("Leather Armor", 1)
        
        
        
        
   
    
    

      
        
       
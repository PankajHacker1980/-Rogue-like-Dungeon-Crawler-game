import random
import time

class DungeonCrawler:
    def __init__(self):
        self.player_health = 100
        self.player_attack = 10
        self.player_defense = 5
        self.player_gold = 0
        self.current_level = 1
        self.max_levels = 5
        self.monsters = {
            "Goblin": {"health": 20, "attack": 8, "defense": 2, "gold": 10},
            "Orc": {"health": 30, "attack": 12, "defense": 5, "gold": 15},
            "Dragon": {"health": 50, "attack": 20, "defense": 10, "gold": 30}
        }
    
    def display_status(self):
        print(f"\nCurrent Stats:")
        print(f"Level: {self.current_level}/{self.max_levels}")
        print(f"Player Health: {self.player_health}")
        print(f"Player Attack: {self.player_attack}")
        print(f"Player Defense: {self.player_defense}")
        print(f"Player Gold: {self.player_gold}")
    
    def explore_level(self):
        print(f"\nExploring Level {self.current_level}...")
        time.sleep(2)
        
        encounter_chance = random.random()
        if encounter_chance < 0.6:
            self.encounter_monster()
        else:
            print("You found nothing of interest.")
    
    def encounter_monster(self):
        monster_name = random.choice(list(self.monsters.keys()))
        monster_stats = self.monsters[monster_name]
        print(f"You encounter a {monster_name}!")
        time.sleep(1)
        
        while self.player_health > 0 and monster_stats["health"] > 0:
            print(f"\nPlayer Health: {self.player_health} | {monster_name} Health: {monster_stats['health']}")
            action = input("Enter 'attack' or 'defend': ").strip().lower()
            
            if action == "attack":
                damage_dealt = max(0, self.player_attack - monster_stats["defense"])
                monster_stats["health"] -= damage_dealt
                print(f"You attack the {monster_name} for {damage_dealt} damage.")
            elif action == "defend":
                damage_taken = max(0, monster_stats["attack"] - self.player_defense)
                self.player_health -= damage_taken
                print(f"The {monster_name} attacks you for {damage_taken} damage.")
            else:
                print("Invalid action. Choose 'attack' or 'defend'.")
                continue
            
            if monster_stats["health"] <= 0:
                print(f"You defeated the {monster_name}!")
                self.player_gold += monster_stats["gold"]
            elif self.player_health <= 0:
                print("You have been defeated!")
                break
        
        time.sleep(1)
    
    def visit_shop(self):
        print("\nWelcome to the shop!")
        print("What would you like to buy?")
        print("1. Health Potion (20 gold) - Restores 30 health")
        print("2. Attack Boost (30 gold) - Increases attack by 5")
        print("3. Defense Boost (25 gold) - Increases defense by 3")
        print("4. Leave Shop")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1" and self.player_gold >= 20:
            self.player_health = min(100, self.player_health + 30)
            self.player_gold -= 20
            print("You bought a Health Potion.")
        elif choice == "2" and self.player_gold >= 30:
            self.player_attack += 5
            self.player_gold -= 30
            print("You bought an Attack Boost.")
        elif choice == "3" and self.player_gold >= 25:
            self.player_defense += 3
            self.player_gold -= 25
            print("You bought a Defense Boost.")
        elif choice == "4":
            print("Leaving the shop.")
        else:
            print("Insufficient gold or invalid choice.")
    
    def play_game(self):
        print("Welcome to Rogue-like Dungeon Crawler!")
        print("Explore dungeons, defeat monsters, and collect loot to progress.")
        
        while self.current_level <= self.max_levels and self.player_health > 0:
            self.display_status()
            action = input("\nEnter your action (explore/shop/quit): ").strip().lower()
            
            if action == "quit":
                print("Exiting the game. Goodbye!")
                break
            elif action == "explore":
                self.explore_level()
            elif action == "shop":
                self.visit_shop()
            else:
                print("Invalid action. Choose explore, shop, or quit.")
            
            if self.player_health > 0:
                self.current_level += 1
        
        if self.player_health <= 0:
            print("Game Over! You have been defeated.")
        elif self.current_level > self.max_levels:
            print(f"Congratulations! You cleared all levels and emerged victorious.")

if __name__ == "__main__":
    game = DungeonCrawler()
    game.play_game()

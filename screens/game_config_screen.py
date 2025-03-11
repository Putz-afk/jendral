import pygame
from utils.helpers import draw_text
from screens.game_screen import GameScreen

class GameConfigScreen:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.config = {
            "character": "Warrior",
            "level": 1,
            "time_limit": 120
        }
        self.selected_option = 0
        self.options = list(self.config.keys())
        
        # Character options
        self.characters = ["Warrior", "Mage", "Archer", "Thief"]
        self.levels = [1, 2, 3, 4, 5]
        self.time_limits = [60, 120, 180, 240, 300]

    def enter(self):
        print("Entered Game Config Screen")

    def exit(self):
        print("Exited Game Config Screen")
        
    def pause(self):
        print("Game Config Screen Paused")
        
    def resume(self):
        print("Game Config Screen Resumed")

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Go back to main menu
                    from screens.main_menu import MainMenu
                    self.state_manager.change_state(MainMenu(self.state_manager))
                    
                # Navigate between options
                elif event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                    
                # Change settings
                elif event.key == pygame.K_LEFT:
                    self.adjust_config(-1)
                elif event.key == pygame.K_RIGHT:
                    self.adjust_config(1)
                    
                # Start game with current config
                elif event.key == pygame.K_RETURN:
                    self.start_game()

    def adjust_config(self, direction):
        current_option = self.options[self.selected_option]
        
        if current_option == "character":
            current_idx = self.characters.index(self.config[current_option])
            new_idx = (current_idx + direction) % len(self.characters)
            self.config[current_option] = self.characters[new_idx]
        elif current_option == "level":
            current_idx = self.levels.index(self.config[current_option])
            new_idx = (current_idx + direction) % len(self.levels)
            self.config[current_option] = self.levels[new_idx]
        elif current_option == "time_limit":
            current_idx = self.time_limits.index(self.config[current_option])
            new_idx = (current_idx + direction) % len(self.time_limits)
            self.config[current_option] = self.time_limits[new_idx]

    def start_game(self):
        # Start the game with the current configuration
        game_screen = GameScreen(self.state_manager)
        # You could pass the configuration to the game screen here
        # game_screen.set_config(self.config)
        self.state_manager.change_state(game_screen)

    def update(self):
        pass

    def render(self, screen):
        screen.fill((70, 40, 40))  # Dark red background
        
        draw_text(screen, "Game Configuration", 50, 50, font_size=48)
        draw_text(screen, "Use UP/DOWN to navigate, LEFT/RIGHT to change", 50, 100, font_size=24)
        draw_text(screen, "Press ENTER to start game or ESC to return to Main Menu", 50, 130, font_size=24)
        
        y_pos = 200
        for i, option in enumerate(self.options):
            display_text = f"{option.replace('_', ' ').title()}: {self.config[option]}"
            
            # Highlight selected option
            color = (255, 255, 0) if i == self.selected_option else (255, 255, 255)
            draw_text(screen, display_text, 50, y_pos, color=color)
            y_pos += 50
            
        # Character preview (just a colored square for simplicity)
        character_colors = {
            "Warrior": (150, 50, 50),
            "Mage": (50, 50, 150),
            "Archer": (50, 150, 50),
            "Thief": (150, 150, 50)
        }
        pygame.draw.rect(screen, character_colors[self.config["character"]], (600, 200, 100, 100))
        draw_text(screen, self.config["character"], 600, 310, font_size=24)
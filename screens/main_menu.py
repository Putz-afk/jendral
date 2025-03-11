import pygame
from screens.game_screen import GameScreen
from screens.settings_screen import SettingsScreen
from screens.game_config_screen import GameConfigScreen
from utils.helpers import draw_text

class MainMenu:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.options = ["Play", "Game Config", "Settings", "Quit"]
        self.selected_option = 0

    def enter(self):
        print("Entered Main Menu")

    def exit(self):
        print("Exited Main Menu")
        
    def pause(self):
        print("Main Menu Paused")
        
    def resume(self):
        print("Main Menu Resumed")

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    self.select_option()

    def select_option(self):
        if self.options[self.selected_option] == "Play":
            self.state_manager.change_state(GameScreen(self.state_manager))
        elif self.options[self.selected_option] == "Game Config":
            self.state_manager.change_state(GameConfigScreen(self.state_manager))
        elif self.options[self.selected_option] == "Settings":
            self.state_manager.change_state(SettingsScreen(self.state_manager))
        elif self.options[self.selected_option] == "Quit":
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))  # Clear screen with black
        
        # Draw title
        draw_text(screen, "Game Menu", 300, 100, font_size=64)
        
        # Draw menu options
        y_pos = 250
        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected_option else (255, 255, 255)
            draw_text(screen, option, 350, y_pos, color=color, font_size=36)
            y_pos += 60
            
        # Draw instructions
        draw_text(screen, "Use UP/DOWN arrows to navigate", 250, 500, font_size=24)
        draw_text(screen, "Press ENTER to select", 250, 530, font_size=24)
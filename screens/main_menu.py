import pygame
from screens.game_screen import GameScreen
from screens.settings_screen import SettingsScreen

class MainMenu:
    def __init__(self, state_manager):
        self.state_manager = state_manager

    def enter(self):
        print("Entered Main Menu")

    def exit(self):
        print("Exited Main Menu")

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.state_manager.change_state(GameScreen(self.state_manager))
                if event.key == pygame.K_2:
                    self.state_manager.change_state(SettingsScreen(self.state_manager))

    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))  # Clear screen with black
        font = pygame.font.Font(None, 36)
        text = font.render("Main Menu - Press 1 to Play, 2 for Settings", True, (255, 255, 255))
        screen.blit(text, (50, 50))
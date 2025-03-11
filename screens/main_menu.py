import pygame
from screens.game_screen import GameScreen
from screens.settings_screen import SettingsScreen
from screens.game_config_screen import GameConfigScreen
from screens.test_screen import TestScreen
from utils.helpers import draw_text, draw_button

class MainMenu:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.options = ["Play", "Game Config", "Settings", "Quit"]
        self.selected_option = 0
        self.mouse_pos = (0, 0)

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
                elif event.key == pygame.K_0:
                    self.state_manager.change_state(TestScreen(self.state_manager))
            elif event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.handle_mouse_click(event.pos)

    def select_option(self):
        if self.options[self.selected_option] == "Play":
            self.state_manager.change_state(GameScreen(self.state_manager))
        elif self.options[self.selected_option] == "Game Config":
            self.state_manager.change_state(GameConfigScreen(self.state_manager))
        elif self.options[self.selected_option] == "Settings":
            self.state_manager.change_state(SettingsScreen(self.state_manager))
        elif self.options[self.selected_option] == "Quit":
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def handle_mouse_click(self, mouse_pos):
        x, y = mouse_pos
        print(f"Mouse clicked at: {x}, {y}")
    
    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))  # Clear screen with black
        
        # Draw title
        draw_text(screen, "Jendral the Game", 300, 100, font_size=64)
        
        # Draw menu options as buttons
        y_pos = 250
        button_width = 200
        button_height = 50
        for i, option in enumerate(self.options):
            def action(index=i):  # Closure to capture the current index
                self.selected_option = index
                self.select_option()
            
            draw_button(
                screen,
                text=option,
                x=350,
                y=y_pos,
                width=button_width,
                height=button_height,
                color=(50, 50, 50),  # Default button color
                hover_color=(100, 100, 100),  # Button color when hovered
                text_color=(255, 255, 255),  # Text color
                mouse_pos=self.mouse_pos,
                action=action
            )
            y_pos += 70  # Spacing between buttons
            
        # Draw instructions
        draw_text(screen, "Use UP/DOWN arrows to navigate", 250, 500, font_size=24)
        draw_text(screen, "Press ENTER to select", 250, 530, font_size=24)
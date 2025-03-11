import pygame
from utils.helpers import draw_text
from utils.settings_manager import SettingsManager

class SettingsScreen:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.settings_manager = SettingsManager()
        self.settings = self.settings_manager.settings
        self.selected_option = 0
        self.options = list(self.settings.keys())
        self.changes_made = False

    def enter(self):
        print("Entered Settings Screen")
        # Load settings from file when entering
        self.settings = self.settings_manager.load_settings()

    def exit(self):
        print("Exited Settings Screen")
        # Save settings when exiting if changes were made
        if self.changes_made:
            self.settings_manager.save_settings(self.settings)
            self.changes_made = False
        
    def pause(self):
        print("Settings Screen Paused")
        
    def resume(self):
        print("Settings Screen Resumed")

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Go back to main menu and save settings
                    if self.changes_made:
                        self.settings_manager.save_settings(self.settings)
                        self.changes_made = False
                    from screens.main_menu import MainMenu
                    self.state_manager.change_state(MainMenu(self.state_manager))
                    
                # Navigate between options
                elif event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                    
                # Change settings
                elif event.key == pygame.K_LEFT:
                    self.adjust_setting(-1)
                elif event.key == pygame.K_RIGHT:
                    self.adjust_setting(1)
                    
                # Reset to defaults
                elif event.key == pygame.K_r:
                    self.settings = self.settings_manager.default_settings.copy()
                    self.changes_made = True

    def adjust_setting(self, direction):
        current_option = self.options[self.selected_option]
        
        if current_option == "music_volume":
            self.settings[current_option] = max(0, min(10, self.settings[current_option] + direction))
            self.changes_made = True
        elif current_option == "sfx_volume":
            self.settings[current_option] = max(0, min(10, self.settings[current_option] + direction))
            self.changes_made = True
        elif current_option == "difficulty":
            difficulties = ["Easy", "Medium", "Hard"]
            current_idx = difficulties.index(self.settings[current_option])
            new_idx = (current_idx + direction) % len(difficulties)
            self.settings[current_option] = difficulties[new_idx]
            self.changes_made = True
        elif current_option == "fullscreen":
            self.settings[current_option] = not self.settings[current_option]
            self.changes_made = True
            # In a real game, you might apply this change immediately:
            # pygame.display.set_mode((800, 600), pygame.FULLSCREEN if self.settings[current_option] else 0)

    def update(self):
        pass

    def render(self, screen):
        screen.fill((50, 50, 70))  # Dark purple background
        
        draw_text(screen, "Settings", 50, 50, font_size=48)
        draw_text(screen, "Use UP/DOWN to navigate, LEFT/RIGHT to change", 50, 100, font_size=24)
        draw_text(screen, "Press ESC to save and return to Main Menu", 50, 130, font_size=24)
        draw_text(screen, "Press R to reset to defaults", 50, 160, font_size=24)
        
        # Show save indicator if changes were made
        if self.changes_made:
            draw_text(screen, "* Unsaved Changes *", 550, 50, font_size=28, color=(255, 255, 0))
        
        y_pos = 200
        for i, option in enumerate(self.options):
            display_text = f"{option.replace('_', ' ').title()}: {self.settings[option]}"
            
            # Highlight selected option
            color = (255, 255, 0) if i == self.selected_option else (255, 255, 255)
            
            # Render volume as bars
            if "volume" in option:
                draw_text(screen, option.replace('_', ' ').title() + ":", 50, y_pos, color=color)
                for j in range(10):
                    bar_color = (0, 255, 0) if j < self.settings[option] else (100, 100, 100)
                    pygame.draw.rect(screen, bar_color, (300 + j * 30, y_pos, 20, 30))
            else:
                draw_text(screen, display_text, 50, y_pos, color=color)
                
            y_pos += 50
import pygame
import os
from screens.main_menu import MainMenu
from utils.state_manager import StateManager
from utils.settings_manager import SettingsManager

def main():
    # Initialize settings before pygame, so we can apply them to the window
    settings_manager = SettingsManager()
    
    pygame.init()
    
    # Apply settings to the game window
    fullscreen = settings_manager.get_setting("fullscreen", False)
    flags = pygame.FULLSCREEN if fullscreen else 0
    screen = pygame.display.set_mode((800, 600), flags)
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    # Create data directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")

    state_manager = StateManager()
    state_manager.change_state(MainMenu(state_manager))

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        state_manager.handle_events(events)
        state_manager.update()
        state_manager.render(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
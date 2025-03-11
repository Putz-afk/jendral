import pygame
from screens.main_menu import MainMenu
from utils.state_manager import StateManager

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

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
import pygame
from utils.helpers import draw_text

class GameScreen:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.player_x = 400
        self.player_y = 300
        self.player_speed = 5

    def enter(self):
        print("Entered Game Screen")

    def exit(self):
        print("Exited Game Screen")
        
    def pause(self):
        print("Game Screen Paused")
        
    def resume(self):
        print("Game Screen Resumed")

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Go back to main menu
                    from screens.main_menu import MainMenu
                    self.state_manager.change_state(MainMenu(self.state_manager))
        
        # Character movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x -= self.player_speed
        if keys[pygame.K_RIGHT]:
            self.player_x += self.player_speed
        if keys[pygame.K_UP]:
            self.player_y -= self.player_speed
        if keys[pygame.K_DOWN]:
            self.player_y += self.player_speed
            
        # Keep player within screen bounds
        self.player_x = max(0, min(self.player_x, 800 - 20))
        self.player_y = max(0, min(self.player_y, 600 - 20))

    def update(self):
        # Game logic would go here
        pass

    def render(self, screen):
        # Clear screen with dark blue
        screen.fill((25, 25, 50))
        
        # Render player (simple rectangle)
        pygame.draw.rect(screen, (255, 0, 0), (self.player_x, self.player_y, 20, 20))
        
        # Draw game instructions
        draw_text(screen, "Game Screen - Use Arrow Keys to Move", 50, 20)
        draw_text(screen, "Press ESC to return to Main Menu", 50, 60, font_size=24)
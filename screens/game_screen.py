import pygame
from utils.helpers import draw_text

class GameScreen:
    def __init__(self, state_manager):
        self.state_manager = state_manager

    def enter(self):
        print("Entered Game Screen")

    def exit(self):
        print("Exited Game Screen")
        
    def pause(self):
        print("Game Screen Paused")
        
    def resume(self):
        print("Game Screen Resumed")

    def handle_events(self, events):
        pass
    
    def update(self):
        pass

    def render(self, screen):
        pass
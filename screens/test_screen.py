import pygame

class TestScreen:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        
    def enter(self):
        print("Entered Test Screen")
        
    def exit(self):
        print("Exited Test Screen")
        
    def pause(self):
        print("Test Screen Paused")
        
    def resume(self):
        print("Test Screen Resumed")
        
    def handle_events(self, events):
        pass
    
    def update(self):
        pass
    
    def render(self, screen):
        pass
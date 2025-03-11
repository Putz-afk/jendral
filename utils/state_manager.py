class StateManager:
    def __init__(self):
        self.state = None
        self.state_stack = []

    def change_state(self, state):
        if self.state:
            self.state.exit()
        self.state = state
        self.state.enter()

    def push_state(self, state):
        if self.state:
            self.state.pause()
        self.state_stack.append(state)
        self.state = state
        self.state.enter()

    def pop_state(self):
        if self.state:
            self.state.exit()
            self.state = None
        
        if len(self.state_stack) > 0:
            self.state = self.state_stack.pop()
            self.state.resume()

    def handle_events(self, events):
        if self.state:
            self.state.handle_events(events)

    def update(self):
        if self.state:
            self.state.update()

    def render(self, screen):
        if self.state:
            self.state.render(screen)
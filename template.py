import pygame

# Eventhandler structure
class EventHandler():
    def __init__(self):
        self.event_mapper: dict[pygame.event.Event.type: function] = {}
    def add(self, event: pygame.event.Event.type, trigger_function, *function_args):
        if event in self.event_mapper:
            self.event_mapper[event] += ([trigger_function, function_args])
            return
        self.event_mapper[event] = ([trigger_function, function_args])
    def update(self):
        for event in pygame.event.get():
            if event.type in self.event_mapper:
                for i in range(0, len(self.event_mapper[event.type]), 2):
                    self.event_mapper[event.type][i](*self.event_mapper[event.type][i+1])

# Global variables
game_enabled = True
screen_dimensions = (400, 400)
frames_per_second = 60

# Initiate PyGame
screen = pygame.display.set_mode(screen_dimensions)
pygame_clock = pygame.time.Clock()

# Function definitions
def game_exit(): # Function to exit game:
    global game_enabled
    pygame.quit()
    game_enabled = False

def game_update(): # Update display, Read events, Limit framerate:
    pygame.display.update()
    pygame_clock.tick(frames_per_second)
    events.update()

def printx(x):
    print(x)

# Initiate EventHandler
events = EventHandler()
events.add(pygame.QUIT, game_exit) 

# Main Loop
while game_enabled:
    screen.fill((0,0,0))
    game_update()

import pygame

# Should game be running? Decided by this class
class GameRunner:
    def __init__(self):
        self.is_running = True
    def quit(self):
        self.is_running = False
        pygame.quit()

# All functions to run before updates
class FunctionQueue:
    def __init__(self):
        self.functions = []
    def add(self, func, params):
        self.functions.append((func, params))
    def call(self):
        for function, parameters in self.functions:
            function(*parameters)

# Eventhandler structure
class EventHandler:
    def __init__(self):
        self.event_mapper: dict[pygame.event.Event.type: function] = {}
    def add(self, event: pygame.event.Event.type, trigger_function, *function_args):
        if event in self.event_mapper:
            self.event_mapper[event] += ([trigger_function, function_args])
            return
        self.event_mapper[event] = ([trigger_function, function_args])
    def update(self):
        global event
        for event in pygame.event.get():
            if event.type in self.event_mapper:
                for i in range(0, len(self.event_mapper[event.type]), 2):
                    self.event_mapper[event.type][i](*self.event_mapper[event.type][i+1])

class InputHandler():
    def __init__(self):
        self.keys_pressed = []
    
    def key_pressed(self):
        global event
        self.keys_pressed.append(pygame.key.name(event.key))

    def key_released(self):
        global event
        self.keys_pressed.remove(pygame.key.name(event.key))

# Gamehandler structure
class GameHandler:
    def __init__(self, updates_per_second, quicksetup: bool = True, eventhandler: EventHandler = EventHandler(), 
                clock: pygame.time.Clock = pygame.time.Clock, gamerunner: GameRunner = GameRunner()):
        self.eventhandler = eventhandler
        if not gamerunner:
            gamerunner = GameRunner()
        self.game = gamerunner
        self.clock = clock
        self.fps = updates_per_second
        self.functionqueue = FunctionQueue()
        self.inputhandler = InputHandler()
        if quicksetup:
            self.eventhandler.add(pygame.KEYDOWN, self.inputhandler.key_pressed)
            self.eventhandler.add(pygame.KEYUP, self.inputhandler.key_released)
            self.eventhandler.add(pygame.QUIT, self.game.quit)

    def add_function(self, function, *parameters):
        self.functionqueue.add(function, parameters)

    def update(self):
        self.functionqueue.call()
        pygame.display.update()
        self.eventhandler.update()
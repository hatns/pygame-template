# Imports
import extension.pyg as pygame

# Global variables
screen_dimensions = (1080, 720)
frames_per_second = 60

# Initiate PyGame
screen = pygame.display.set_mode(screen_dimensions)

# Initiate GameHandler
gamehandler = pygame.GameHandler(frames_per_second)

# Main Loop
while gamehandler.game.is_running:
    gamehandler.update()
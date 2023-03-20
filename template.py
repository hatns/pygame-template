# Imports
import extension.pyg as pyg
import pygame

# Global variables
screen_dimensions = (700, 500)
frames_per_second = 60

# Initiate PyGame
window = pygame.display.set_mode(screen_dimensions)

# Initiate GameHandler
gamehandler = pyg.GameHandler(frames_per_second)

# Main Loop
while gamehandler.game.is_running:
    gamehandler.update()
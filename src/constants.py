import pygame

# Screen dimensions
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Load images
CROWN = pygame.transform.scale(pygame.image.load('../assets/crown.png'), (44, 25))

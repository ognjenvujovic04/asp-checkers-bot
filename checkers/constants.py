import pygame

WIDTH, HEIGHT = 700, 700
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
WHITE_PIECE = (252,251,240)
WHITE = (252,251,240)
BLACK_PIECE = (73,77,78)
BLACK = (41,45,46)
GREY = (128,128,128)
BLUE = (0,0,255)

CROWN = pygame.transform.scale(pygame.image.load('../assets/crown.png'), (44, 25))
LOGO_PATH = "../assets/checkers-logo.png" 
import pygame
import sys
from game import Game
from constants import WIDTH, HEIGHT

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(screen)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = game.get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

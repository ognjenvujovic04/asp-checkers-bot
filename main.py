import pygame
import os
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game
from checkers.menu import main_menu

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():    
    mode = main_menu() # 0 for jumping optional, 1 for jumping mandatory
    
    pygame.init()
    FPS = 60
     
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Checkers')

    clock = pygame.time.Clock()


    game = Game(WIN)

    run = True
    while run:
        clock.tick(FPS)

        if game.winner() is not None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()

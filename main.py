import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE_PIECE
from checkers.game import Game
from checkers.menu import main_menu

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def display_winner(screen, winner):
    if winner == WHITE_PIECE:
        winner_name = "White"
    else:
        winner_name = "Black"
    font = pygame.font.Font(None, 74)
    text = font.render(f"{winner_name} wins!", True, (255, 255, 255))
    
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    background_rect = text_rect.inflate(20, 20)  

    pygame.draw.rect(screen, (0, 0, 0), background_rect)

    screen.blit(text, text_rect)
    pygame.display.update()

def main():    
    mode = main_menu() # 0 for jumping optional, 1 for jumping mandatory
    
    pygame.init()
    FPS = 60
    
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Checkers')

    clock = pygame.time.Clock()

    game = Game(WIN)

    run = True
    winner = None
    while run:
        clock.tick(FPS)

        if game.winner() is not None:
            winner = game.winner()
            display_winner(WIN, winner)
            pygame.time.delay(5000)  # Delay for 5 seconds
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

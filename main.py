import pygame
import time
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE_PIECE
from checkers.game import Game
from checkers.menu import main_menu
from bot.minimax import minimax

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def calculate_depth(position):
    num_figures = position.white_left + position.white_kings + position.black_left + position.black_kings
    thresholds = [10, 6, 3]  
    depths = [6, 7, 8]         
    for threshold, depth in zip(thresholds, depths):
        if num_figures >= threshold:
            return depth
    return 9

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
    mode = main_menu()  # 0 for optional, 1 for mandatory skipping

    pygame.init()
    FPS = 60

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Checkers')

    clock = pygame.time.Clock()

    game = Game(window, mode)

    run = True
    winner = None

    transposition_table = {}

    while run:
        clock.tick(FPS)

        if game.turn == WHITE_PIECE:
            depth = calculate_depth(game.get_board().position)
            start_time = time.time()
            value, new_position = minimax(game.get_board().position, depth, True, float('-inf'), float('inf'), game.mode, transposition_table)
            
            end_time = time.time()

            game.bot_move(new_position)
            print("Bot move eval: " + str(value))
            print("Computation time: {:.2f} seconds".format(end_time - start_time))

        if game.winner() is not None:
            winner = game.winner()
            display_winner(window, winner)
            pygame.time.delay(5000)
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
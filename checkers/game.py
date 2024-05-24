import pygame
from checkers.constants import BLACK_PIECE, WHITE_PIECE, BROWN, SQUARE_SIZE
from checkers.board import Board

class Game:
    def __init__(self, window, mode):
        self._init()
        self.mode = mode
        self.window = window
    
    def update(self):
        self.board.draw(self.window)
        if self.selected:
            self.draw_selected_piece_ring(self.selected_row, self.selected_col)
            self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.selected_row = None
        self.selected_col = None
        self.board = Board()
        self.turn = BLACK_PIECE
        self.valid_moves = {}
        self.possible_jumps = False

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(self.selected_row, self.selected_col, row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.selected_row = row
            self.selected_col = col
            self.valid_moves = self.board.position.get_valid_moves_position(row, col, self.mode)[0]
            return True
            
        return False

    def _move(self, start_row, end_row, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0:
            for move in self.valid_moves:
                if row == move[2] and col == move[3] and self.mode ==0:
                    self.board.move(self.selected, row, col)
                    skipped = self.valid_moves[(start_row, end_row, row, col)]
                    if skipped:
                        self.board.remove(skipped)
                    self.selected = None
                    self.change_turn()
                elif row == move[2] and col == move[3] and self.mode == 1:
                    if self.possible_jumps == True and len(self.valid_moves[move]) != 0:
                        self.board.move(self.selected, row, col)
                        skipped = self.valid_moves[(start_row, end_row, row, col)]
                        if skipped:
                            self.board.remove(skipped)
                        self.selected = None
                        self.change_turn()
                    elif self.possible_jumps == False:
                        self.board.move(self.selected, row, col)
                        skipped = self.valid_moves[(start_row, end_row, row, col)]
                        if skipped:
                            self.board.remove(skipped)
                        self.selected = None
                        self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            if self.mode == 0:
                start_row, start_col, row, col = move
                pygame.draw.circle(self.window, BROWN, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 20)
            elif self.possible_jumps == True and len(moves[move]) != 0:
                start_row, start_col, row, col = move
                pygame.draw.circle(self.window, BROWN, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 20)
            elif self.possible_jumps == False:
                start_row, start_col, row, col = move
                pygame.draw.circle(self.window, BROWN, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 20)

    def draw_selected_piece_ring(self, row, col):
        x = col * SQUARE_SIZE + SQUARE_SIZE // 2
        y = row * SQUARE_SIZE + SQUARE_SIZE // 2
        pygame.draw.circle(self.window, BROWN, (x, y), SQUARE_SIZE // 2 - 10, 6)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK_PIECE:
            self.turn = WHITE_PIECE
        else:
            self.turn = BLACK_PIECE
        self.possible_jumps = False
        for piece in self.board.get_all_pieces(self.turn):
            if self.board.position.get_valid_moves_position(piece.row, piece.col, self.mode)[1] == 1:
                self.possible_jumps = True
                break
            
    def get_board(self):
        return self.board
    
    def bot_move(self, board):
        self.board = board
        self.change_turn()

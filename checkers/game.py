import pygame
from checkers.constants import BLACK_PIECE, WHITE_PIECE, BROWN, SQUARE_SIZE
from checkers.board import Board

class Game:
    def __init__(self, window):
        self._init()
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

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.selected_row = row
            self.selected_col = col
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.selected = None
            self.valid_moves = {}
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
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
            
    def get_board(self):
        return self.board
    
    def bot_move(self, board):
        self.board = board
        self.change_turn()

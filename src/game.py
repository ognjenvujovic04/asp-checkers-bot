import pygame
from board import Board
from constants import RED, WHITE

class Game:
    def __init__(self, screen):
        self._init()
        self.screen = screen

    def _init(self):
        self.board = Board()
        self.turn = RED
        self.selected_piece = None

    def update(self):
        self.board.draw(self.screen)
        pygame.display.flip()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected_piece:
            result = self._move(row, col)
            if not result:
                self.selected_piece = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected_piece = piece
            return True
        return False

    def _move(self, row, col):
        piece = self.selected_piece
        if piece and self.board.move(piece, row, col):
            self.change_turn()
            return True
        return False

    def change_turn(self):
        self.turn = WHITE if self.turn == RED else RED

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y // self.board.SQUARE_SIZE
        col = x // self.board.SQUARE_SIZE
        return row, col

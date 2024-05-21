import pygame
from piece import Piece
from constants import BLACK, RED, WHITE, ROWS, COLS, SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = []
        self.create_board()

    def draw(self, screen):
        self.draw_squares(screen)
        for row in self.board:
            for piece in row:
                if piece != 0:
                    piece.draw(screen)

    def draw_squares(self, screen):
        screen.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(screen, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row % 2 == ((col + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def get_piece(self, row, col):
        return self.board[row][col]

    def move(self, piece, row, col):
        if self.valid_move(piece, row, col):
            self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
            piece.move(row, col)
            if row == 0 or row == ROWS - 1:
                piece.make_king()
            return True
        return False

    def valid_move(self, piece, row, col):
        # Implement valid move logic here
        return True

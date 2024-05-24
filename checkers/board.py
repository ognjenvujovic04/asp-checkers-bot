import pygame
from .square import Square
from .constants import BLACK, ROWS, WHITE_PIECE, BLACK_PIECE, SQUARE_SIZE, COLS, WHITE
from .piece import Piece
from .position import Position

class Board:
    def __init__(self):
        
        #raspored figura
        self.position = Position()
        
        # crtanje tabele
        self.board = []
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0
        self.create_board()
    
    def draw_squares(self, window):
        window.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, WHITE, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.position.pieces[piece.row][piece.col], self.position.pieces[row][col] = Square.EMPTY, piece.type
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            self.position.pieces[row][col] = Square.WHITE_KING if piece.color == WHITE_PIECE else Square.BLACK_KING
            if piece.color == WHITE:
                self.white_kings += 1
                self.position.white_kings += 1
            else:
                self.black_kings += 1 
                self.position.black_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE_PIECE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLACK_PIECE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
        
    def draw(self, window):
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)

    def remove(self, pieces):
        for cordinates in pieces:
            piece = self.board[cordinates[0]][cordinates[1]]
            self.board[piece.row][piece.col] = 0
            self.position.pieces[piece.row][piece.col] = Square.EMPTY
            if piece != 0:
                if piece.color == BLACK_PIECE:
                    self.black_left -= 1
                    self.position.black_left -= 1
                else:
                    self.white_left -= 1
                    self.position.white_left -= 1
    
    def winner(self):
        if self.position.winner() != None:
            return self.position.winner()
        return None 
    
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces
        
    
    
    def update_board(self, position):
        black_kings = white_kings = 0
        self.position = position
        for row in range(8):
            for col in range(8):
                if position.pieces[row][col] == Square.WHITE_KING:
                    white_kings += 1
                elif position.pieces[row][col] == Square.BLACK_KING:
                    black_kings += 1
                if self.board[row][col] != 0:
                    if self.position.pieces[row][col] != self.board[row][col].type:
                        if self.position.pieces[row][col] != Square.EMPTY:
                            if self.position.pieces[row][col] == Square.WHITE_KING:
                                self.board[row][col] = Piece(row, col, WHITE_PIECE)
                                self.board[row][col].make_king()
                            elif self.position.pieces[row][col] == Square.BLACK_KING:
                                self.board[row][col] = Piece(row, col, BLACK_PIECE)
                                self.board[row][col].make_king()
                            else:
                                self.board[row][col] = Piece(row, col, get_color(self.position.pieces[row][col]))
                        else:
                            self.board[row][col] = 0
                elif self.position.pieces[row][col] != Square.EMPTY:
                    if self.position.pieces[row][col] == Square.WHITE_KING:
                        self.board[row][col] = Piece(row, col, WHITE_PIECE)
                        self.board[row][col].make_king()
                    elif self.position.pieces[row][col] == Square.BLACK_KING:
                        self.board[row][col] = Piece(row, col, BLACK_PIECE)
                        self.board[row][col].make_king()
                    else:
                        if row == 7 and self.position.pieces[row][col] == Square.BLACK_PIECE:
                            self.board[row][col] = Piece(row, col, WHITE_PIECE)
                            self.board[row][col].make_king()
                        if row == 0 and self.position.pieces[row][col] == Square.WHITE_PIECE:
                            self.board[row][col] = Piece(row, col, BLACK_PIECE)
                            self.board[row][col].make_king()
                        self.board[row][col] = Piece(row, col, get_color(self.position.pieces[row][col]))
                    
        self.black_kings = black_kings
        self.position.black_kings = black_kings
        self.white_kings = white_kings
        self.position.white_kings = white_kings
        self.black_left = position.black_left
        self.position.black_left = position.black_left
        self.white_left = position.white_left
        self.position.white_left = position.white_left
        
        return self
    
def get_color(square):
        if square == Square.WHITE_PIECE or square == Square.WHITE_KING:
            return WHITE_PIECE
        elif square == Square.BLACK_PIECE or square == Square.BLACK_KING:
            return BLACK_PIECE
        return 0
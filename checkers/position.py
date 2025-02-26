from checkers.square import Square
from checkers.constants import WHITE_PIECE, BLACK_PIECE


class Position:
    def __init__(self):
        self.pieces = [
            [Square.EMPTY, Square.WHITE_PIECE, Square.EMPTY, Square.WHITE_PIECE, Square.EMPTY, Square.WHITE_PIECE, Square.EMPTY, Square.WHITE_PIECE],
            [Square.WHITE_PIECE, Square.EMPTY, Square.WHITE_PIECE, Square.EMPTY, Square.WHITE_PIECE, Square.EMPTY, Square.WHITE_PIECE, Square.EMPTY],
            [Square.EMPTY, Square.WHITE_PIECE, Square.EMPTY, Square.WHITE_PIECE, Square.EMPTY, Square.WHITE_PIECE, Square.EMPTY, Square.WHITE_PIECE],
            [Square.EMPTY, Square.EMPTY, Square.EMPTY, Square.EMPTY, Square.EMPTY, Square.EMPTY, Square.EMPTY, Square.EMPTY],
            [Square.EMPTY, Square.EMPTY, Square.EMPTY, Square.EMPTY, Square.EMPTY, Square.EMPTY, Square.EMPTY, Square.EMPTY],
            [Square.BLACK_PIECE, Square.EMPTY, Square.BLACK_PIECE, Square.EMPTY, Square.BLACK_PIECE, Square.EMPTY, Square.BLACK_PIECE, Square.EMPTY],
            [Square.EMPTY, Square.BLACK_PIECE, Square.EMPTY, Square.BLACK_PIECE, Square.EMPTY, Square.BLACK_PIECE, Square.EMPTY, Square.BLACK_PIECE],
            [Square.BLACK_PIECE, Square.EMPTY, Square.BLACK_PIECE, Square.EMPTY, Square.BLACK_PIECE, Square.EMPTY, Square.BLACK_PIECE, Square.EMPTY]
        ]
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0
        
    def winner(self):
        if self.black_left == 0 and self.black_kings == 0:
            return WHITE_PIECE
        elif self.white_left == 0 and self.white_kings == 0:
            return BLACK_PIECE
        else:
            move_counter_white = 0
            move_counter_black = 0
            for row in range(8):
                for col in range(8):
                    if self.pieces[row][col] == Square.WHITE_PIECE or self.pieces[row][col] == Square.WHITE_KING:
                        if len(self.get_valid_moves(row, col, 0)[0]) != 0:
                            move_counter_white += 1
                    if self.pieces[row][col] == Square.BLACK_PIECE or self.pieces[row][col] == Square.BLACK_KING:
                        if len(self.get_valid_moves(row, col, 0)[0]) != 0:
                            move_counter_black += 1
            if move_counter_black == 0:
                return WHITE_PIECE
            elif move_counter_white == 0:
                return BLACK_PIECE
        return None
        
    def position_to_string(self):
        return "".join(str(self.pieces[row][col].value) for row in range(len(self.pieces)) for col in range(len(self.pieces[row])) if (row + col) % 2 == 1)


    # pisem fukciju za validne poteze koja ce koristiti rijecnjik sa kljucem touple (x1,y1,x2,y2) gde je x1,y1 pocetna pozicija a x2,y2 krajnja pozicija
    # i vrednostima koje su figure koje se skacu i sklanjaju sa table
    
    #funkcija vraca rijecnjik sa validnim potezima i 0 ako nije bilo skakanja i 1 ako je bilo skakanja
    
    def get_valid_moves(self, row, col, mode):
        moves = {}
        type = self.pieces[row][col]
        if type == Square.WHITE_PIECE:
            #jump moves
            if row + 2 < 8 and col - 2 >= 0 and (self.pieces[row + 1][col - 1] == Square.BLACK_PIECE or self.pieces[row + 1][col - 1] == Square.BLACK_KING) and self.pieces[row + 2][col - 2] == Square.EMPTY:
                moves[(row, col, row + 2, col - 2)] = [(row + 1, col - 1)]
            if row + 2 < 8 and col + 2 < 8 and (self.pieces[row + 1][col + 1] == Square.BLACK_PIECE or self.pieces[row + 1][col + 1] == Square.BLACK_KING) and self.pieces[row + 2][col + 2] == Square.EMPTY:
                moves[(row, col, row + 2, col + 2)] = [(row + 1, col + 1)]
            
            if len(moves) != 0 and mode == 1:
                return moves,1
            
            #regular moves
            if row + 1 < 8 and col - 1 >= 0 and self.pieces[row + 1][col - 1] == Square.EMPTY:
                moves[(row, col, row + 1, col - 1)] = []
            if row + 1 < 8 and col + 1 < 8 and self.pieces[row + 1][col + 1] == Square.EMPTY:
                moves[(row, col, row + 1, col + 1)] = []
            

                
        elif type == Square.BLACK_PIECE:
            #jump moves
            if row - 2 >= 0 and col - 2 >= 0 and (self.pieces[row - 1][col - 1] == Square.WHITE_PIECE or self.pieces[row - 1][col - 1] == Square.WHITE_KING) and self.pieces[row - 2][col - 2] == Square.EMPTY:
                moves[(row, col, row - 2, col - 2)] = [(row - 1, col - 1)]
            if row - 2 >= 0 and col + 2 < 8 and (self.pieces[row - 1][col + 1] == Square.WHITE_PIECE or self.pieces[row - 1][col + 1] == Square.WHITE_KING) and self.pieces[row - 2][col + 2] == Square.EMPTY:
                moves[(row, col, row - 2, col + 2)] = [(row - 1, col + 1)]

            if len(moves) != 0 and mode == 1:
                return moves,1

            #regular moves
            if row - 1 >= 0 and col - 1 >= 0 and self.pieces[row - 1][col - 1] == Square.EMPTY:
                moves[(row, col, row - 1, col - 1)] = []
            if row - 1 >= 0 and col + 1 < 8 and self.pieces[row - 1][col + 1] == Square.EMPTY:
                moves[(row, col, row - 1, col + 1)] = []
            
               
        elif type == Square.BLACK_KING:
            #jump moves
            if row - 2 >= 0 and col - 2 >= 0 and (self.pieces[row - 1][col - 1] == Square.WHITE_PIECE or self.pieces[row - 1][col - 1] == Square.WHITE_KING) and self.pieces[row - 2][col - 2] == Square.EMPTY:
                moves[(row, col, row - 2, col - 2)] = [(row - 1, col - 1)]
            if row - 2 >= 0 and col + 2 < 8 and (self.pieces[row - 1][col + 1] == Square.WHITE_PIECE or self.pieces[row - 1][col + 1] == Square.WHITE_KING) and self.pieces[row - 2][col + 2] == Square.EMPTY:
                moves[(row, col, row - 2, col + 2)] = [(row - 1, col + 1)]
            
            #backward jump moves
            if row + 2 < 8 and col - 2 >= 0 and (self.pieces[row + 1][col - 1] == Square.WHITE_PIECE or self.pieces[row + 1][col - 1] == Square.WHITE_KING) and self.pieces[row + 2][col - 2] == Square.EMPTY:
                moves[(row, col, row + 2, col - 2)] = [(row + 1, col - 1)]
            if row + 2 < 8 and col + 2 < 8 and (self.pieces[row + 1][col + 1] == Square.WHITE_PIECE or self.pieces[row + 1][col + 1] == Square.WHITE_KING) and self.pieces[row + 2][col + 2] == Square.EMPTY:
                moves[(row, col, row + 2, col + 2)] = [(row + 1, col + 1)]
                   
            if len(moves) != 0 and mode == 1:
                return moves,1       
                   
            #regular moves
            if row - 1 >= 0 and col - 1 >= 0 and self.pieces[row - 1][col - 1] == Square.EMPTY:
                moves[(row, col, row - 1, col - 1)] = []
            if row - 1 >= 0 and col + 1 < 8 and self.pieces[row - 1][col + 1] == Square.EMPTY:
                moves[(row, col, row - 1, col + 1)] = []
            
            #backward regular moves
            if row + 1 < 8 and col - 1 >= 0 and self.pieces[row + 1][col - 1] == Square.EMPTY:
                moves[(row, col, row + 1, col - 1)] = []
            if row + 1 < 8 and col + 1 < 8 and self.pieces[row + 1][col + 1] == Square.EMPTY:
                moves[(row, col, row + 1, col + 1)] = []
            
        elif type == Square.WHITE_KING:
            #jump moves
            if row + 2 < 8 and col - 2 >= 0 and (self.pieces[row + 1][col - 1] == Square.BLACK_PIECE or self.pieces[row + 1][col - 1] == Square.BLACK_KING) and self.pieces[row + 2][col - 2] == Square.EMPTY:
                moves[(row, col, row + 2, col - 2)] = [(row + 1, col - 1)]
            if row + 2 < 8 and col + 2 < 8 and (self.pieces[row + 1][col + 1] == Square.BLACK_PIECE or self.pieces[row + 1][col + 1] == Square.BLACK_KING) and self.pieces[row + 2][col + 2] == Square.EMPTY:
                moves[(row, col, row + 2, col + 2)] = [(row + 1, col + 1)]
            
            #backward jump moves
            if row - 2 >= 0 and col - 2 >= 0 and (self.pieces[row - 1][col - 1] == Square.BLACK_PIECE or self.pieces[row - 1][col - 1] == Square.BLACK_KING) and self.pieces[row - 2][col - 2] == Square.EMPTY:
                moves[(row, col, row - 2, col - 2)] = [(row - 1, col - 1)]
            if row - 2 >= 0 and col + 2 < 8 and (self.pieces[row - 1][col + 1] == Square.BLACK_PIECE or self.pieces[row - 1][col + 1] == Square.BLACK_KING) and self.pieces[row - 2][col + 2] == Square.EMPTY:
                moves[(row, col, row - 2, col + 2)] = [(row - 1, col + 1)]
            
            if len(moves) != 0 and mode == 1:
                return moves,1
            
            #regular moves
            if row + 1 < 8 and col - 1 >= 0 and self.pieces[row + 1][col - 1] == Square.EMPTY:
                moves[(row, col, row + 1, col - 1)] = []
            if row + 1 < 8 and col + 1 < 8 and self.pieces[row + 1][col + 1] == Square.EMPTY:
                moves[(row, col, row + 1, col + 1)] = []
            
            #backward regular moves
            if row - 1 >= 0 and col - 1 >= 0 and self.pieces[row - 1][col - 1] == Square.EMPTY:
                moves[(row, col, row - 1, col - 1)] = []
            if row - 1 >= 0 and col + 1 < 8 and self.pieces[row - 1][col + 1] == Square.EMPTY:
                moves[(row, col, row - 1, col + 1)] = []
            
                 
        return moves,0
    
    
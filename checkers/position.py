from checkers.square import Square


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

        

    # pisem fukciju za validne poteze koja ce koristiti rijecnjik sa kljucem touple (x1,y1,x2,y2) gde je x1,y1 pocetna pozicija a x2,y2 krajnja pozicija
    # i vrednostima koje su figure koje se skacu i sklanjaju sa table
    
    def get_valid_moves_position(self, row, col):
        moves = {}
        type = self.pieces[row][col]
        if type == Square.WHITE_PIECE:
            #regular moves
            if row + 1 >= 0 and col - 1 >= 0 and self.pieces[row + 1][col - 1] == Square.EMPTY:
                moves[(row, col, row + 1, col - 1)] = []
            if row + 1 >= 0 and col + 1 < 8 and self.pieces[row + 1][col + 1] == Square.EMPTY:
                moves[(row, col, row + 1, col + 1)] = []
            
            #jump moves
            if row + 2 <= 8 and col - 2 >= 0 and (self.pieces[row + 1][col - 1] == Square.BLACK_PIECE or self.pieces[row + 1][col - 1] == Square.BLACK_KING) and self.pieces[row + 2][col - 2] == Square.EMPTY:
                moves[(row, col, row + 2, col - 2)] = [(row + 1, col - 1)]
            if row + 2 <= 8 and col + 2 < 8 and (self.pieces[row + 1][col + 1] == Square.BLACK_PIECE or self.pieces[row + 1][col + 1] == Square.BLACK_KING) and self.pieces[row + 2][col + 2] == Square.EMPTY:
                moves[(row, col, row + 2, col + 2)] = [(row + 1, col + 1)]
                
        elif type == Square.BLACK_PIECE:
            #regular moves
            if row - 1 >= 0 and col - 1 >= 0 and self.pieces[row - 1][col - 1] == Square.EMPTY:
                moves[(row, col, row - 1, col - 1)] = []
            if row - 1 >= 0 and col + 1 < 8 and self.pieces[row - 1][col + 1] == Square.EMPTY:
                moves[(row, col, row - 1, col + 1)] = []
            
            #jump moves
            if row - 2 >= 0 and col - 2 >= 0 and (self.pieces[row - 1][col - 1] == Square.WHITE_PIECE or self.pieces[row - 1][col - 1] == Square.WHITE_KING) and self.pieces[row - 2][col - 2] == Square.EMPTY:
                moves[(row, col, row - 2, col - 2)] = [(row - 1, col - 1)]
            if row - 2 >= 0 and col + 2 < 8 and (self.pieces[row - 1][col + 1] == Square.WHITE_PIECE or self.pieces[row - 1][col + 1] == Square.WHITE_KING) and self.pieces[row - 2][col + 2] == Square.EMPTY:
                moves[(row, col, row - 2, col + 2)] = [(row - 1, col + 1)]
                
        elif type == Square.BLACK_KING:
            #regular moves
            if row - 1 >= 0 and col - 1 >= 0 and self.pieces[row - 1][col - 1] == Square.EMPTY:
                moves[(row, col, row - 1, col - 1)] = []
            if row - 1 >= 0 and col + 1 < 8 and self.pieces[row - 1][col + 1] == Square.EMPTY:
                moves[(row, col, row - 1, col + 1)] = []
            #jump moves
            if row - 2 >= 0 and col - 2 >= 0 and (self.pieces[row - 1][col - 1] == Square.BLACK_PIECE or self.pieces[row - 1][col - 1] == Square.BLACK_KING) and self.pieces[row - 2][col - 2] == Square.EMPTY:
                moves[(row, col, row - 2, col - 2)] = [(row - 1, col - 1)]

                
            if row - 2 >= 0 and col + 2 < 8 and (self.pieces[row - 1][col + 1] == Square.WHITE_PIECE or self.pieces[row - 1][col + 1] == Square.WHITE_PIECE) and self.pieces[row - 2][col + 2] == Square.EMPTY:
                moves[(row, col, row - 2, col + 2)] = [(row - 1, col + 1)]
                
        return moves
    
    
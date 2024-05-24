from copy import deepcopy
from checkers.constants import WHITE_PIECE, BLACK_PIECE
from checkers.square import Square

def minimax(position, depth, maximizing_player, alpha, beta, mode):
    if depth == 0 or position.winner() is not None:
        return evaluate(position), position

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        possible_possitions = get_possible_positions(position, WHITE_PIECE, mode)
        if len(possible_possitions) == 0:
            return -1000, None
        for move in possible_possitions:
            position_eval= minimax(move, depth - 1, False, alpha, beta, mode)[0]
            max_eval = max(max_eval, position_eval)
            if max_eval == position_eval:
                best_move = move
            alpha = max(alpha, position_eval)
            if beta < alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        possible_possitions = get_possible_positions(position, BLACK_PIECE, mode)
        if len(possible_possitions) == 0:
            return -1000, None
        for move in possible_possitions:
            position_eval= minimax(move, depth - 1, True, alpha, beta, mode)[0]
            min_eval = min(min_eval, position_eval)
            if min_eval == position_eval:
                best_move = move
            beta = min(beta, position_eval)
            if beta < alpha:
                break
        return min_eval, best_move

def evaluate(position):
    print ((position.white_left - position.black_left) + (position.white_kings - position.black_kings)*0.5)
    return (position.white_left - position.black_left) + (position.white_kings - position.black_kings)*0.5

def simulate_move(move, position, skip):
    position.pieces[move[2]][move[3]], position.pieces[move[0]][move[1]]  = position.pieces[move[0]][move[1]], position.pieces[move[2]][move[3]]
    if position.pieces[move[2]][move[3]] == Square.BLACK_PIECE and move[2] == 0:
        position.pieces[move[2]][move[3]] = Square.BLACK_KING
        position.black_kings += 1
    elif position.pieces[move[2]][move[3]] == Square.WHITE_PIECE and move[2] == 7:
        position.pieces[move[2]][move[3]] = Square.WHITE_KING
        position.white_kings += 1
    if skip:
        skip = skip[0]
        if position.pieces[skip[0]][skip[1]] == Square.BLACK_PIECE:
            position.black_left -= 1
        elif position.pieces[skip[0]][skip[1]] == Square.WHITE_PIECE:
            position.white_left -= 1
        elif position.pieces[skip[0]][skip[1]] == Square.BLACK_KING:
            position.black_left -= 1
            position.black_kings -= 1
        else:
            position.white_left -= 1
            position.white_kings -= 1
        position.pieces[skip[0]][skip[1]] = Square.EMPTY
    return position

def get_possible_positions(position, color, mode):
    postions = []
    
    for row in range(8):
        for col in range(8):
            square = position.pieces[row][col]
            if square.value != 0 and  square.value % 2 == 0 and color == BLACK_PIECE:
                valid_moves = position.get_valid_moves(row, col, mode)[0]
                for move, skip in valid_moves.items():
                    temp_position = deepcopy(position)
                    new_position = simulate_move(move, temp_position, skip)
                    postions.append(new_position)
            elif square.value % 2 != 0 and color == WHITE_PIECE:
                valid_moves = position.get_valid_moves(row, col, mode)[0]
                for move, skip in valid_moves.items():
                    temp_position = deepcopy(position)
                    new_position = simulate_move(move, temp_position, skip)
                    postions.append(new_position)
    
    return postions

# def find_next_move(self, board):
#     best_move = None
    
#     for square in board.position.pieces:
#         if square.value % 2 != 0 and self.turn == WHITE_PIECE:
#             valid_moves = board.position.get_valid_moves(square.row, square.col, self.mode)
#             for move, skip in valid_moves.items():
#                 temp_position = deepcopy(board)
#                 new_position = simulate_move(move, temp_position, skip)
#                 postions.append(new_position)
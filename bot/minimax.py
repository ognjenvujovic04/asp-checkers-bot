from copy import deepcopy
from checkers.constants import WHITE_PIECE, BLACK_PIECE

def minimax(board, depth, maximizing_player, alpha, beta):
    if depth == 0 or board.winner() is not None:
        return evaluate(board), board

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_possible_moves(board, WHITE_PIECE):
            eval = minimax(move, depth - 1, False, alpha, beta)[0]
            max_eval = max(max_eval, eval)
            if max_eval == eval:
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_possible_moves(board, BLACK_PIECE):
            eval = minimax(move, depth - 1, True, alpha, beta)[0]
            min_eval = min(min_eval, eval)
            if min_eval == eval:
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def evaluate(board):
    print (board.white_left - board.black_left)
    return (board.white_left - board.black_left)

def simulate_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def get_possible_moves(board, color):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)
    
    return moves
from copy import deepcopy
from checkers.constants import WHITE_PIECE, BLACK_PIECE

def minimax(board, depth, maximizing_player, alpha, beta):
    if depth == 0 or board.winner() is not None:
        return evaluate(board), board

    if maximizing_player:
        best_eval = float('-inf')
        best_move = None
        for move in get_possible_moves(board, WHITE_PIECE):
            board_eval= minimax(move, depth - 1, False, alpha, beta)[0]
            print(board_eval)
            best_eval = max(best_eval, board_eval)
            if best_eval == board_eval:
                best_move = move
            # alpha = max(alpha, best_eval)
            # if beta <= alpha:
            #    break
        return best_eval, best_move
    else:
        best_eval = float('inf')
        best_move = None
        for move in get_possible_moves(board, BLACK_PIECE):
            board_eval= minimax(move, depth - 1, True, alpha, beta)[0]
            best_eval = min(best_eval, board_eval)
            if best_eval == board_eval:
                best_move = move
            # beta = min(beta, best_eval)
            # if beta <= alpha:
            #     break
        return best_eval, best_move

def evaluate(board):
    return (board.white_left - board.black_left) + (board.white_kings - board.black_kings)*0.5
    # if board.winner() == WHITE_PIECE:
    #     return float('inf')
    # elif board.winner() == BLACK_PIECE:
    #     return float('-inf')
    # else:
    #     white_score = [0, 0, 0, 0, 0]
    #     black_score = [0, 0, 0, 0, 0]
    #     for row in range(8):
    #         for col in range(8):
    #             piece = board.get_piece(col, row)
    #             if piece != 0:
    #                 if piece.color == WHITE_PIECE:
    #                     if piece.king:
    #                         white_score[1] += 1
    #                     else:
    #                         white_score[0] += 1
    #                     if row == 7:
    #                         white_score[2] += 1
    #                     if row == 3 or row == 4:
    #                         if 2 <= col <= 5:
    #                             white_score[3] += 1
    #                         else:
    #                             white_score[4] += 1
    #                 else:
    #                     if piece.king:
    #                         black_score[1] += 1
    #                     else:
    #                         black_score[0] += 1
    #                     if row == 0:
    #                         black_score[2] += 1
    #                     if row == 3 or row == 4:
    #                         if 2 <= col <= 5:
    #                             black_score[3] += 1
    #                         else:
    #                             black_score[4] += 1
                                
    #     weights = [5, 7.5, 4, 2.5, 0.5]
    #     score = 0
    #     for i in range(len(weights)):
    #         score += weights[i] * (black_score[i] - white_score[i])
    #     return score           
        
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
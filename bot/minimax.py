from copy import deepcopy
from checkers.constants import WHITE_PIECE, BLACK_PIECE
from checkers.square import Square

def minimax(position, depth, maximizing_player, alpha, beta, mode, transposition_table):
    position_str = position.position_to_string()

    if position_str in transposition_table and transposition_table[position_str][1].position_to_string() != position.position_to_string():
        return transposition_table[position_str]

    if depth == 0 or position.winner() is not None:
        evaluation = evaluate(position)
        transposition_table[position_str] = (evaluation, position)
        return evaluation, position

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        possible_positions = get_possible_positions(position, WHITE_PIECE, mode)
        if len(possible_positions) == 0:
            return -1000, None
        for move in possible_positions:
            position_eval = minimax(move, depth - 1, False, alpha, beta, mode, transposition_table)[0]
            max_eval = max(max_eval, position_eval)
            if max_eval == position_eval:
                best_move = move
            alpha = max(alpha, position_eval)
            if beta < alpha:
                break
        transposition_table[position_str] = (max_eval, best_move)
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        possible_positions = get_possible_positions(position, BLACK_PIECE, mode)
        if len(possible_positions) == 0:
            return 1000, None
        for move in possible_positions:
            position_eval = minimax(move, depth - 1, True, alpha, beta, mode, transposition_table)[0]
            min_eval = min(min_eval, position_eval)
            if min_eval == position_eval:
                best_move = move
            beta = min(beta, position_eval)
            if beta < alpha:
                break
        transposition_table[position_str] = (min_eval, best_move)
        return min_eval, best_move

def evaluate(position):
    white_score = [0, 0, 0, 0, 0, 0, 0]
    blacke_score = [0, 0, 0, 0, 0, 0, 0]
    white_score[0] = position.white_left - position.white_kings
    blacke_score[0] = position.black_left - position.black_kings
    white_score[1] = position.white_kings
    blacke_score[1] = position.black_kings
    for row in range(8):
        for col in range(8):
            square = position.pieces[row][col]
            if square.value == 0:
                continue
            if square.value % 2 == 0: # black
                if row == 7: #zadnji red
                    blacke_score[2] += 1
                    blacke_score[6] += 1 
                if row == 3 or row == 4: #sredina
                    if 2 <= col <= 5:
                        blacke_score[3] += 1
                    else:
                        blacke_score[4] += 1
                if 7 > row > 0 and 0 < col < 7: #ugrozene crne figure
                    if (position.pieces[row - 1][col - 1] == Square.WHITE_PIECE or position.pieces[row - 1][col - 1] == Square.WHITE_KING) \
                    and position.pieces[row + 1][col + 1] == Square.EMPTY:
                        blacke_score[5] += 1
                    if (position.pieces[row - 1][col + 1] == Square.WHITE_PIECE or position.pieces[row - 1][col + 1] == Square.WHITE_KING) \
                    and position.pieces[row + 1][col - 1] == Square.EMPTY:
                        blacke_score[5] += 1
                if row < 7:
                    if col == 0 or col == 7:
                        blacke_score[6] += 1
                    elif (position.pieces[row + 1][col - 1] == Square.BLACK_PIECE or position.pieces[row + 1][col - 1] == Square.BLACK_KING\
                    or position.pieces[row + 1][col - 1] == Square.WHITE_PIECE) and (position.pieces[row + 1][col + 1] == Square.BLACK_PIECE\
                    or position.pieces[row + 1][col + 1] == Square.BLACK_KING or position.pieces[row + 1][col + 1] == Square.WHITE_PIECE):
                        blacke_score[6] += 1  
            else: # white
                if row == 0: #zadnji red
                    white_score[2] += 1
                    white_score[6] += 1
                if row == 3 or row == 4: #sredina
                    if 2 <= col <= 5:
                        white_score[3] += 1
                    else:
                        white_score[4] += 1
                if 0 < row < 7 and 0 < col < 7: #ugrozene bele figure
                    if (position.pieces[row + 1][col - 1] == Square.BLACK_PIECE or position.pieces[row + 1][col - 1] == Square.BLACK_KING) \
                    and position.pieces[row - 1][col + 1] == Square.EMPTY:
                        white_score[5] += 1
                    if (position.pieces[row + 1][col + 1] == Square.BLACK_PIECE or position.pieces[row + 1][col + 1] == Square.BLACK_KING) \
                    and position.pieces[row - 1][col - 1] == Square.EMPTY:
                        white_score[5] += 1
                if row > 0:
                    if col == 0 or col == 7:
                        white_score[6] += 1
                    elif (position.pieces[row - 1][col - 1] == Square.WHITE_PIECE or position.pieces[row - 1][col - 1] == Square.WHITE_KING\
                    or position.pieces[row - 1][col - 1] == Square.BLACK_PIECE) and (position.pieces[row - 1][col + 1] == Square.WHITE_PIECE\
                    or position.pieces[row - 1][col + 1] == Square.WHITE_KING or position.pieces[row - 1][col + 1] == Square.BLACK_PIECE):
                        white_score[6] += 1
    weights = [5, 7.75, 4, 2.5, 0.5, -3, 3]
    eval_score = 0
    for i in range(7):
        eval_score += weights[i] * (white_score[i] - blacke_score[i])
    #print(eval_score)
    return eval_score

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

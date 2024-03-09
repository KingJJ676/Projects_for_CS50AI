"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # count X, O and EMPTY
    X_count = 0
    O_count = 0

    for row in board:
        for cell in row:
            if cell == X:
                X_count += 1
            elif cell == O:
                O_count += 1

    # check for terminal (0)
    if terminal(board) == True:
        return 0

    # if same number or X is less, X's turn
    if X_count <= O_count:
        return X

    # elif O is less, O's turn
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # defining a set to return results
    actions = set()

    # check for terminal
    if terminal(board) == True:
        return set()

    # go over the board and record into actions
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                action = (i, j)
                actions.add(action)
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # check if the action is valid
    valid_actions = actions(board)
    if action not in valid_actions:
        raise Exception("Invalid aciton")

    # deep copy the current board
    new_board = copy.deepcopy(board)

    # update new_board
    mark = str(player(board))
    i, j = action[0], action[1]
    new_board[i][j] = mark

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # if wins horizontally
    for row in board:
        if all(cell == X for cell in row):
            return X
        if all(cell == O for cell in row):
            return O

    # if wins vertically
    for column in range(3):
        if all(row[column] == X for row in board):
            return X
        if all(row[column] == O for row in board):
            return O

    # if wins diagonally (top-left to bottom-right)
    if all(board[i][i] == X for i in range(len(board))):
        return X
    if all(board[i][i] == O for i in range(len(board))):
        return O

    # if wins diagonally (top-right to bottom-left)
    if all(board[i][2 - i] == X for i in range(len(board))):
        return X
    if all(board[i][2 - i] == O for i in range(len(board))):
        return O

    # if tie or game still in progress
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if someone won
    if winner(board) != None:
        return True

    # game still in progress
    progressing = False
    for row in board:
        for cell in row:
            if cell == EMPTY:
                progressing = True
                return False

    # board filled
    if progressing == False:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def maximize(board):
        v = -float("inf")
        optimal = None
        
        # check for terminal state
        if terminal(board) == True:
            return utility(board), None

        for action in actions(board):
            min_v, _ = minimize(result(board, action))
            if v < min_v:
                v = min_v
                optimal = action
        return v, optimal

    def minimize(board):
        v = float("inf")
        optimal = None

        # check for terminal state
        if terminal(board) == True:
            return utility(board), None

        for action in actions(board):
            max_v, _ = maximize(result(board, action))
            if v > max_v:
                v = max_v
                optimal = action
        return v, optimal


    # if terminal state
    if terminal(board) == True:
        return None

    # check if player should maximize or minimize
    if player(board) == X:
        _, max_optimal = maximize(board)
        return max_optimal
    if player(board) == O:
        _, min_optimal = minimize(board)
        return min_optimal

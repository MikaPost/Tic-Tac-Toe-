"""
This file is for our new theme: tic tac toe
Create by: Miqayel Postoyan
Date: 15 April
"""
import random

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]


def print_board(board_data):
    """
        Function: print_board
        Brief: print_board
        Params: board_data (list): The 2D list representing the game board.
        Return:	None
    """
    for row in board_data:
        print(" | ".join(row))
        print("-" * 9)


def check(board_data):
    """
        Function: check
        Brief: checks the sheet to see if someone has won or not
        Params: board_data (list): The 2D list representing the game board.
        Return:	True and False
    """
    for row in range(3):
        if board_data[row][0] == board_data[row][1] == board_data[row][2] and board_data[row][0] in ["x", "o"]:
            return True
    for col in range(3):
        if board_data[0][col] == board_data[1][col] == board_data[2][col] and board_data[0][col] in ["x", "o"]:
            return True
    if board_data[0][0] == board_data[1][1] == board_data[2][2] and board_data[0][0] in ["x", "o"]:
        return True
    if board_data[0][2] == board_data[1][1] == board_data[2][0] and board_data[0][2] in ["x", "o"]:
        return True
    return False



def player1():
    """
        Function: player1
        Brief: Allows Player X to make a move on the board.
        Params: None
        Return:	board (list)
    """
    print("Player X")
    player1_column, player1_row = int(input("Enter column(1, 2, 3)")), int(input("Enter row(1, 2, 3)"))
    if board[player1_column - 1][player1_row - 1] == "-":
        board[player1_column - 1][player1_row - 1] = "x"
    else:
        print("that box is already taken.Choose another")
        player1()
    print_board(board)
    return board


def player2():
    """
        Function: player2
        Brief: bot to make a move on the board.
        Params: None
        Return:	board (list)
    """
    print("Player o")
    player2_column, player2_row = int(input("Enter o column(1, 2, 3)")), int(input("Enter row(1, 2, 3)"))
    if board[player2_column - 1][player2_row - 1] == "-":
        board[player2_column - 1][player2_row - 1] = "o"
    else:
        print("that box is already taken.Choose another")
        player2()
    print_board(board)
    return board


def two_player():
    """
        Function: two_player
        Brief: function if there are 2 players
        Params: None
        Return:	None
    """
    print_board(board)
    while True:
        b = player1()
        if check(b):
            end("x")
            break
        c = player2()
        if check(c):
            end("o")
            break


def robot():
    """
        Function: robot
        Brief: function if there are 1 player and 1 bot
        Params: None
        Return:	board (list)
    """
    robot_column, robot_row = random.choice([1, 2, 3]), random.choice([1, 2, 3])
    if board[robot_column - 1][robot_column - 1] == "-":
        board[robot_row - 1][robot_row - 1] = "o"
    else:
        robot()
    print("Player o(bot)")
    print_board(board)
    return board


def one_player():
    """
        Function: one_player
        Brief: function if there are 1 player and 1 bot
        Params: None
        Return:	None
    """
    print_board(board)
    while True:
        b = player1()
        if check(b):
            end("x")
            break
        c = robot()
        if check(c):
            end("o")
            break


def end(winner):
    """
        Function: end
        Brief: end of the game who wins?
        Params: winner (x/o)
        Return:	None
    """
    if winner == "x":
        print("__________________________________________________")
        print("x won!!!")
        print("__________________________________________________")
    else:
        print("__________________________________________________")
        print("o won!!!")
        print("__________________________________________________")


def main():
    """
    Function: main
    Brief: Entry point
    """
    print("one or two player?")
    player = input("enter one or two")
    if player in "two" or player in "2":
        two_player()
    else:
        one_player()

if __name__ == "__main__":
    main()

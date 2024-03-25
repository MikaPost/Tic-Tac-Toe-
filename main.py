import random

a = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]


def print_board(a):
    for row in a:
        print(" | ".join(row))
        print("-" * 9)


def check(a):
    for row in range(3):
        if a[row][0] == a[row][1] == a[row][2] and a[row][0] in ["x", "o"]:
            return True
    for col in range(3):
        if a[0][col] == a[1][col] == a[2][col] and a[0][col] in ["x", "o"]:
            return True
    if a[0][0] == a[1][1] == a[2][2] and a[0][0] in ["x", "o"]:
        return True
    if a[0][2] == a[1][1] == a[2][0] and a[0][2] in ["x", "o"]:
        return True
    return False



def player1():
    print("Player X")
    player1_column, player1_row = int(input("Enter column(1, 2, 3)")), int(input("Enter row(1, 2, 3)"))
    if a[player1_column - 1][player1_row - 1] == "-":
        a[player1_column - 1][player1_row - 1] = "x"
    else:
        print("that box is already taken.Choose another")
        player1()
    print_board(a)
    return a


def player2():
    print("Player o")
    player2_column, player2_row = int(input("Enter o column(1, 2, 3)")), int(input("Enter row(1, 2, 3)"))
    if a[player2_column - 1][player2_row - 1] == "-":
        a[player2_column - 1][player2_row - 1] = "o"
    else:
        print("that box is already taken.Choose another")
        player2()
    print_board(a)
    return a


def two_player():
    print_board(a)
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
    robot_column, robot_row = random.choice([1, 2, 3]), random.choice([1, 2, 3])
    if a[robot_column - 1][robot_column - 1] == "-":
        a[robot_row - 1][robot_row - 1] = "o"
    else:
        robot()
    print("Player o(bot)")
    print_board(a)
    return a


def one_player():
    print_board(a)
    while True:
        b = player1()
        if check(b):
            end("x")
            break
        c = robot()
        if check(c):
            end("o")
            break


def end(b):
    if b == "x":
        print("__________________________________________________")
        print("x won!!!")
        print("__________________________________________________")
    else:
        print("__________________________________________________")
        print("o won!!!")
        print("__________________________________________________")


def main():
    print("one or two player?")
    player = input("enter one or two")
    if player == "two" or player == "2":
        two_player()
    else:
        one_player()

if __name__ == "__main__":
    main()
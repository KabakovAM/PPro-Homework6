from random import randint
__all__ = ['diagonals']

def diagonals(data, board):        
    a = int(data[0])
    b = int(data[2])
    while not(a == 0 or b == 0):
        a -= 1
        b -= 1
        temp = '{}:{}'.format(a, b)
        if temp in board:
            return False
    a = int(data[0])
    b = int(data[2])
    while not(a == 9 or b == 9):
        a += 1
        b += 1
        temp = '{}:{}'.format(a, b)
        if temp in board:
            return False
    a = int(data[0])
    b = int(data[2])
    while not(a == 9 or b == 0):
        a += 1
        b -= 1
        temp = '{}:{}'.format(a, b)
        if temp in board:
            return False
    a = int(data[0])
    b = int(data[2])
    while not(a == 0 or b == 9):
        a -= 1
        b += 1
        temp = '{}:{}'.format(a, b)
        if temp in board:
            return False
    return True


def check(board):
    d_check = 0        
    gor = sorted(list(i[0] for i in board))
    vert = sorted(list(i[2] for i in board))
    for i in range(len(board) - 1):
        if gor[i] == gor[i+1] or vert[i] == vert[i+1]:
            return False
    for i in range(len(board)):
        if not diagonals(board[i], board):
            d_check = 1
    if d_check == 1:
        return False
    return True


def create_check():
    board = []
    ok_check = 0
    while ok_check != 1:
        for _ in range(8):
            queen = '{}:{}'.format(randint(1, 8), randint(1, 8))
            board.append(queen)
        if not check(board):
            board.clear()
        else:
            ok_check = 1
    return board


if __name__ == '__main__':
    for _ in range(4):
        print(create_check())
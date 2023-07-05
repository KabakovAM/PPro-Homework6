def diagonals(data, board):        
    a = int(data[0])
    b = int(data[2])
    while not(a == 0 or b == 0):
        a -= 1
        b -= 1
        temp = "{}:{}".format(a, b)
        if temp in board:
            return False
    a = int(data[0])
    b = int(data[2])
    while not(a == 9 or b == 9):
        a += 1
        b += 1
        temp = "{}:{}".format(a, b)
        if temp in board:
            return False
    a = int(data[0])
    b = int(data[2])
    while not(a == 9 or b == 0):
        a += 1
        b -= 1
        temp = "{}:{}".format(a, b)
        if temp in board:
            return False
    a = int(data[0])
    b = int(data[2])
    while not(a == 0 or b == 9):
        a -= 1
        b += 1
        temp = "{}:{}".format(a, b)
        if temp in board:
            return False
    return True

def check(board):
    d_check = 0        
    gor = sorted(list(i[0] for i in board))
    vert = sorted(list(i[2] for i in board))
    for i in range(7):
        if gor[i] == gor[i+1] or vert[i] == vert[i+1]:
            return False
    for i in range(len(board)):
        if not diagonals(board[i], board):
            d_check = 1
    if d_check == 1:
        return False
    return True


board = ['1:4', '2:8', '3:1', '4:3', '5:6', '6:2', '7:7', '8:5']
print(check(board))
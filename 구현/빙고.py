# 빅준 2578 빙고

numbers = []
say_numbers = []
board = [[0, 0, 0, 0, 0] for i in range(5)]

def find_number(a, board):
    for i in range(5):
        for j in range(5):
            if numbers[i][j] == a:
                board[i][j] = 1
                return board

def check_line(board):
    total = 0
    for i in range(5):
        if board[i][0] == 1 and board[i][1] == 1 and board[i][2] == 1 and board[i][3] == 1 and board[i][4] == 1:
            total += 1
        if board[0][i] == 1 and board[1][i] == 1 and board[2][i] == 1 and board[3][i] == 1 and board[4][i] == 1:
            total += 1
    if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1 and board[3][3] == 1 and board[4][4] == 1:
        total += 1
    if board[4][0] == 1 and board[3][1] == 1 and board[2][2] == 1 and board[1][3] == 1 and board[0][4] == 1:
        total += 1
    return total


for _ in range(5):
    number = list(map(int, input().split()))
    numbers.append(number)

for _ in range(5):
    number = list(map(int, input().split()))
    say_numbers.extend(number)

for x in range(25):
    board = find_number(say_numbers[x], board)
    total = check_line(board)
    if total >= 3:
        print(x+1)
        break
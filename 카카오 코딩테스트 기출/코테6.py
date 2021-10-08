import numpy as np

def solution(board, skill):
    board = np.array(board)
    a, b = board.shape
    for i in skill:
        z = np.zeros((a, b),dtype='int')
        type_data,r1, c1, r2, c2, degree = i
        data = np.array([degree]*((r2-r1+1)*(c2-c1+1)))
        reshape_data = data.reshape((r2-r1+1),(c2-c1+1))
        z = np.pad(reshape_data,((r1,a-r2-1),(c1,b-c2-1)),'constant',constant_values=0)
        if type_data == 1:
            board -= z
        else:
            board += z
    answer = 0
    for i in range(a):
        for j in range(b):
            if board[i][j] > 0:
                answer += 1


    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))
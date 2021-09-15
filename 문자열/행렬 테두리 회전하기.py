from collections import deque
def solution(rows, columns, queries):
    answer = []
    result = []
    for i in range(0, rows):
        array = [j+(columns*i) for j in range(1, columns+1)]
        result.append(array)
    for query in queries:
        r1, c1, r2, c2 = query
        data_list = []
        temp_side_list = []
        for i in range(r1 - 1, r2):
            if i == r1 - 1:
                data_list.extend(result[i][c1-1:c2])
            elif i == r2 - 1:
                if c1-2 < 0:
                    data_list.extend(result[i][c2-1::-1])
                else:
                    data_list.extend(result[i][c2-1:c1-2:-1])
            else:
                data_list.append(result[i][c2-1])
                temp_side_list.insert(0, result[i][c1-1])
        data_list.extend(temp_side_list)
        data_list.insert(0, data_list[-1])
        del data_list[-1]
        dq = deque(data_list)
        answer.append(min(dq))
        for j in range(r1-1,r2):
            for k in range(c1-1,c2):
                if j == r1 - 1:
                    result[j][k] = dq.popleft()
                elif j == r2 - 1:
                    result[j][k] = dq.pop()
                else:
                    if k == c1-1:
                        result[j][k] = dq.pop()
                    elif k == c2-1:
                        result[j][k] = dq.popleft()

    return answer


print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
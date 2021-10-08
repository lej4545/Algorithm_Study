def solution(weights, head2head):
    result = []
    num = len(weights)
    for i in range(num):
        cnt, win,lose = 0, 0, 0
        for j in range(num):
            if head2head[i][j] == 'W':
                win += 1
                if weights[i] < weights[j]:
                    cnt += 1
            elif head2head[i][j] == 'L':
                lose += 1
        if win + lose == 0:
            result += [[0, cnt, weights[i], i+1]]
        else:
            result += [[win/(win + lose)*100, cnt, weights[i], i+1]]
    result = sorted(result, key = lambda x:(x[0],x[1],x[2]), reverse = True)
    print(result)
    answer = [k[3] for k in result]
    print(answer)
    return answer
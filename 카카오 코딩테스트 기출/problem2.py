def move(costs, row, col, cost, xcost, ycost, cost_list):
    cost += costs[row][col]

    if row != len(costs)-1:
        move(costs, row+1, col, cost - ycost, xcost, ycost, cost_list)
    else:
        cost_list.append(cost)

    if col != len(costs[0])-1:
        move(costs, row, col+1, cost - xcost, xcost, ycost, cost_list)

def solution(costs, xcost, ycost):
    answer = -1
    row = 0
    col = 0
    cost = costs[row][col]
    cost_list = []
    move(costs, row+1, col, cost - ycost, xcost, ycost, cost_list)
    move(costs, row, col+1, cost - xcost, xcost, ycost, cost_list)
    max_cost = max(cost_list)
    if max_cost <= 0:
        answer = 0
    else:
        answer = max_cost
    return answer

print(solution([[0,0,0],[0,0,0],[0,0,1]], 0, 0))
print(solution([[1,2,3],[4,5,6],[7,8,9]], 1, 1))
print(solution([[1,2,3],[4,5,6],[7,8,9]], 100, 0))
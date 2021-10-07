import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global graph
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

def solution(m, n, k):
    global graph
    graph = []
    for _ in range(n):
        graph_temp = [0] * m
        graph.append(graph_temp)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    return graph

input = sys.stdin.readline
case = int(input())
result = []
for case in range(case):
    result_temp = 0
    m, n, k = map(int, input().split())
    graph = solution(m, n, k)
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result_temp += 1
    result.append(result_temp)

for i in result:
    print(i)

import sys

def bfs(graph, start, visited):
    global friends
    queue = []
    result = []
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            queue.append(i)
            result.append(i)
            visited[i] = True
    for j in queue:
        for m in graph[j]:
            if not visited[m]:
                result.append(m)
                visited[m] = True
    friends.append(len(result))

graph = [[]]
num = int(sys.stdin.readline())

for idx in range(num):
    a = input()
    graph_temp = []
    for id in range(num):
        if a[id] == 'Y':
            graph_temp.append(id+1)
    graph.append(graph_temp)

friends = []
for i in range(1, num+1):
    visited = [False] * (num + 1)
    bfs(graph, i, visited)
print(max(friends))
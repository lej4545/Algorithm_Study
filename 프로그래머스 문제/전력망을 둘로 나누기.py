# 특정 원소가 속한 집함을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, wires):
    result = []
    for i in range(len(wires)):
        parent = [0] * (n + 1)
        for j in range(1, n + 1):
            parent[j] = j

        for wire in range(len(wires)):
            if i != wire:
                union_parent(parent, wires[wire][0], wires[wire][1])

        for i1 in range(1, n+1):
            find_parent(parent, i1)

        num_dict = {}
        for idx, val in enumerate(parent):
            if idx != 0:
                if val in num_dict:
                    num_dict[val].append(idx)
                else:
                    num_dict[val] = [idx]
        total = []
        print(parent)
        print(num_dict)
        for value in num_dict.values():
            total.append(len(value))
        result_temp = abs(total[0] - total[1])
        result.append(result_temp)
    answer = min(result)
    return answer

n = 6
wires = [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]]
print(solution(n, wires))

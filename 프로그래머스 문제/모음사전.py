from itertools import product

def solution(word):
    result = []
    alpha = ['A','E','I','O','U']
    for i in range(6):
        for a in product(alpha, repeat=i):
            a = ''.join(a)
            result.append(a)
    result.sort()
    answer = result.index(word)
    return answer

word = 'AAAAE'
print(solution(word))
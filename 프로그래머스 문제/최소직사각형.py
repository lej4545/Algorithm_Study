import numpy as np


# def solution(sizes):
#     for i in range(len(sizes)):
#         if sizes[i][0] < sizes[i][1]:
#             sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
#
#     sizes = np.array(sizes)
#     result = np.apply_along_axis(lambda a: np.max(a), 0, sizes)
#     result = result.tolist()
#     answer = result[0] * result[1]
#     return answer


def solution(sizes):

    col1 = 0
    col2 = 0

    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        col1 = max(col1, sizes[i][0])
        col2 = max(col2, sizes[i][1])

    answer = col1 * col2
    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))
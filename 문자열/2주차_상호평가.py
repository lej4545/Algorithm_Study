import numpy as np
def solution(scores):
    answer = ''
    scores_np = np.array(scores)
    for i in range(len(scores_np)):
        col = scores_np[:,i]
        max_val = col[np.where(col == col.max())]
        max_idx = np.argmax(col)
        min_val = col[np.where(col == col.min())]
        min_idx = np.argmin(col)
        if max_idx == i and len(max_val) == 1:
            scores_np[i][i] = 0
        if min_idx == i and len(min_val) == 1:
            scores_np[i][i] = 0
    for i in range(len(scores_np)):
        col = scores_np[:,i]
        avg_list = col[np.where(col > 0)]
        avg_value = avg_list.mean()
        if avg_value >= 90:
            score = 'A'
        elif avg_value >= 80:
            score = 'B'
        elif avg_value >= 70:
            score = 'C'
        elif avg_value >= 50:
            score = 'D'
        else:
            score = 'F'
        answer += score
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
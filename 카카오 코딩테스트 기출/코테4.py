from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    number_list = list(range(0, 11))
    lion_result_list = []
    result_dict = {}
    for cwr in combinations_with_replacement(number_list, n):
        lion_result = [0] * 11
        for i in cwr:
            lion_result[10-i] += 1
        lion_result_list.append(lion_result)
    for lion_result_data in lion_result_list:
        lion_score = 0
        apeach_score = 0
        for idx in range(11):
            if lion_result_data[idx] > info[idx]:
                lion_score += (10 - idx)
            elif lion_result_data[idx] < info[idx]:
                apeach_score += (10 - idx)
            elif lion_result_data[idx] == info[idx] and lion_result_data[idx] != 0:
                apeach_score += (10 - idx)
        if lion_score - apeach_score >= 0:
            diff = lion_score - apeach_score
            if diff in result_dict:
                result_dict[diff].append(lion_result_data)
            else:
                result_dict[diff] = [lion_result_data]
    if len(result_dict) != 0:
        result_dict = sorted(result_dict.items(),key=lambda x:x[0],reverse=True)
        max_score_list = result_dict[0][1]
        answer_list = sorted(max_score_list, key=lambda x:(x[-1],x[-2],x[-3],x[-4],x[-5],x[-6],x[-7],x[-8],x[-9],x[-10]),reverse=True)
        answer = answer_list[0]
    else:
        answer = [-1]
    return answer

n = 1
info = [1,0,0,0,0,0,0,0,0,0,0]
print(solution(n, info))
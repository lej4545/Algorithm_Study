import numpy as np
def solution(table, languages, preference):
    lan = ["SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME"]
    a_table = []
    scores = []
    result = []
    for i in table:
        i = i.split()[1:]
        temp = []
        for language in languages:
            if language in i:
                idx = 5 - (i.index(language))
            else:
                idx = 0
            temp.append(idx)
        a_table.append(temp)
    a_table = np.array(a_table)
    for i in a_table:
        score = sum(i * preference)
        scores.append(score)
    max_score = max(scores)
    for j in range(len(scores)):
        if scores[j] == max_score:
            result.append(lan[j])
    result.sort()
    answer = result[0]
    return answer

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7,5,5]
print(solution(table, languages, preference))

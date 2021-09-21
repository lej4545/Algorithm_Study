def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    reported_dict = {}
    user_dict = {}
    for id in id_list:
        user_dict[id] = []
    for content in report:
        user = content.split(" ")[0]
        reported_user = content.split(" ")[1]
        user_dict[user].append(reported_user)

        if reported_user in reported_dict:
            reported_dict[reported_user] += 1

        else:
            reported_dict[reported_user] = 1
    malicious_user_list = []
    for reported_user in reported_dict:
        if reported_dict[reported_user] >= k:
            malicious_user_list.append(reported_user)

    for user in user_dict:
        mail_num = 0
        for malicious_user in user_dict[user]:
            if malicious_user in malicious_user_list:
                mail_num += 1
        answer.append(mail_num)
    return answer

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))
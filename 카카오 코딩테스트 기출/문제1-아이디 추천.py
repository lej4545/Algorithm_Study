def solution(new_id):
    # 1단계
    step1 = new_id.lower()

    # 2단계
    step2 = ''
    for i in step1:
        if ('a' <= i <= 'z') or ('0' <= i <= '9') or (i == '-') or (i == '_') or (i == '.'):
            step2 += i
        else:
            continue

    step3 = step2
    while True:
        step3 = step3.replace("..", ".")
        if step3.find("..") == -1:
            break

    step4 = list(step3)
    if step4[0] == '.':
        step4[0] = ''
    if step4[len(step4) - 1] == '.':
        step4[len(step4) - 1] = ''
    step4 = "".join(step4)

    if len(step4) == 0:
        step5 = "a"
    else:
        step5 = step4

    if len(step5) >= 16:
        step6 = step5[:15]
        if step6[-1] == ".":
            step6 = step6[:len(step6) - 1]
    else:
        step6 = step5

    if len(step6) <= 2:
        while len(step6) < 3:
            step6 += step6[-1]

    answer = step6
    return answer
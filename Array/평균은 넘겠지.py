case = int(input())
for i in range(case):
    input_data = list(map(int,input().split()))
    n = input_data[0]
    scores = input_data[1:]

    scores_avg = sum(scores) / n
    count = 0
    for j in scores:
        if j > scores_avg:
            count += 1

    print("{0:.3%}".format(count/n))
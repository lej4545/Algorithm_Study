n, m = map(int, input().split())

cnt = 0
sample = 'WBWBWBWB'
row_odd = sample + sample[:m-8]
row_oven = sample[1:] + sample[:m-7]

for i in range(1,n+1):
    input_data = input()
    for j in range(m):
        if i % 2 == 0:
            if row_oven[j] != input_data[j]:
                cnt += 1

        else:
            if row_odd[j] != input_data[j]:
                cnt += 1
print(cnt)
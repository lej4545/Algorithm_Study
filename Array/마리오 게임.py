n = int(input())
data = list(map(int, input().split()))

peak_high_list = []
peak_low_list = []
sum_eat_odd = 0
sum_eat_oven = 0
for i in range(1,n-2):
    if data[i-1] < data[i] and data[i] > data[i+1]:
        peak_high_list.append([i,data[i]])
if data[0] > data[1]:
    peak_high_list.append([0,data[0]])
if data[-2] < data[-1]:
    peak_high_list.append([n-1,data[-1]])

peak_high_list = sorted(peak_high_list, key=lambda x:x[0])

for i in peak_high_list:
    sum_eat_odd += i[1]

for j in range(len(peak_high_list)-1):
    slice_list = data[peak_high_list[j][0]+1:peak_high_list[j+1][0]]
    peak_low_list.append(min(slice_list))

sum_eat_oven = sum(peak_low_list)

print(peak_high_list)
print(peak_low_list)
print(sum_eat_odd-sum_eat_oven)
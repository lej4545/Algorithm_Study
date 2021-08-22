a = int(input())
num = 0
variable_add = 1
count = 0
while num < a:
    num += variable_add
    count += 1
    variable_add += 1

first_index = num-(variable_add-1)+1
N_th = a - first_index
if count % 2 == 0:
    a = 1 + N_th
    b = count - N_th
else:
    a = count - N_th
    b = 1 + N_th

print('%d/%d'%(a,b))

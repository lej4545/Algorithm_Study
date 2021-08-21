Croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

alpha = input()

for i in Croatia:
    alpha = alpha.replace(i,"1")

print(len(alpha))
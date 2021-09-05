def dfs_permutation(array, r):
    i_array = [(x, i) for i, x in enumerate(array)]
    print(i_array)
    stack = [[i] for _, i in i_array]
    return_list = []

    while len(stack) > 0:
        current = stack.pop(0)
        for i in range(len(i_array)): # 4번만큼 반복
            if i not in current:
                temp = current + [i_array[i][1]]
                if len(temp) == r:
                    elements = []
                    for idx in temp:
                        elements.append(i_array[idx][0])
                    return_list.extend([elements])
                else:
                    stack.append(temp)
    return return_list


print(dfs_permutation("ABCD", 3))
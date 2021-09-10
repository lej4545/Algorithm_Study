# n = int(input())
# num = 666
# cnt = 0
# while True:
#     a = str(num)
#     if '666' in a:
#         cnt += 1
#         if cnt == n:
#             print(num)
#             break
#     num += 1

import sys


def main():
    n = int(sys.stdin.readline())

    lst = list(range(10000))
    set_lst = set()
    for i in lst:
        print(i)
        x = str(i).zfill(4)
        for j in range(5):
            y = x[:j] + "666" + x[j:]
            set_lst.add(int(y))

    print(sorted(list(set_lst)))


if __name__ == "__main__":
    main()
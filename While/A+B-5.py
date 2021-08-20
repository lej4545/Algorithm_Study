# result = 1
# while True:
#     a, b = map(int, input().split())
#     result = a + b
#     if result == 0:
#         break
#     print(result)

while True:
    try:
        a, b = map(int, input().split())
        result = a + b
        print(result)
    except:
        break
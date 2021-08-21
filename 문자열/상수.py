def upside_down(n):
   first_num = n % 10
   middle_num = (n % 100) // 10
   last_num = n // 100
   result = first_num * 100 + middle_num * 10 + last_num
   return result

a, b = map(int, input().split())
upside_down_a = upside_down(a)
upside_down_b = upside_down(b)
if upside_down_a > upside_down_b:
   print(upside_down_a)
else:
   print(upside_down_b)


# 정수 n, m을 입력 받기
n, m = list(map(int, input().split()))

# n개의 화폐 단위 정보를 입력받기
a = [0]* n
for i in range(n):
    a[i] = int(input())

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] + [10001] * (m+1)

for i in range(n):
    for j in range(a[i], m+1):
        if d[j-a[i]] != 10001: # i-k원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-a[i]] + 1)
# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
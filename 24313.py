#24313번 알고리즘 수업 - 점근적 표기 1

a, b = map(int, input().split())
c = int(input())
n = int(input())

sum = a*n + b

if sum <= c*n and c >= a:
    print(1)
else:
    print(0)

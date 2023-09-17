#2231번 분해합

n = int(input())
s = 0

for i in range(1, n+1):
    a = list(map(int, str(i)))
    s = i + sum(a)
    if s == n:
        print(i)
        break
    if i == n:
        print(0)

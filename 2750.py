#2750번 수 정렬하기

n = int(input())

a = []

for i in range(n):
    b = int(input())
    a.append(b)

a = sorted(a)

for i in range(len(a)):
    print(a[i])

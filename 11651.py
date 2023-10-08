#11651번 좌표 정렬하기 2

n = int(input())

a = []
for _ in range (n):
    a.append(list(map(int, input().split())))

for i in range(n):
    a[i][0], a[i][1] = a[i][1], a[i][0]

b = sorted(a)

for i in range(n):
    b[i][0], b[i][1] = b[i][1], b[i][0]

for i in range(n):
    print(*b[i])

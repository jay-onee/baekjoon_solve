#11650번 좌표 정렬하기

n = int(input())

a = []
for _ in range (n):
    a.append(list(map(int, input().split())))

b = sorted(a)
for i in range(n):
    print(*b[i])

#10811번 바구니 뒤집기

N, M = map(int, input().split())

x = list(range(1, N+1))

def preverse(a, b):
    tmp = []
    y = 0
    for i in range(a, b+1):
        tmp.append(x[i-1])
    tmp.reverse()
    del x[a-1:b]
    for j in range(a, b+1):
        x.insert(j-1, tmp[y])
        y += 1

for a in range(0, M):
    i, j = map(int, input().split())
    preverse(i, j)

print(*x)

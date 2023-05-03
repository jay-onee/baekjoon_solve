#10810번 공 넣기

N, M = map(int, input().split())

mylist = list(range(0, N))

for c in range(0, N):
    mylist.pop(c)
    mylist.insert(c, 0)

for a in range(0, M):
    i, j, k = map(int, input().split())
    for b in range(i-1, j):
        mylist.pop(b)
        mylist.insert(b, k)

print(*mylist)

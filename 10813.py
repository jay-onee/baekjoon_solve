#10813 공 바꾸기

N, M = map(int, input().split())

mylist = list(range(1, N+1))

for k in range (0, M):
    i, j = map(int, input().split())
    a = mylist[i-1]
    b = mylist[j-1]
    mylist[i-1] = b
    mylist[j-1] = a

print(*mylist)

#2562번 최댓값 문제

list = []
for i in range (0, 9):
    a = int(input())
    list.append(a)

print(max(list))
print(list.index(max(list))+1)

#10807번 개수세기
a = int(input())
b = list(map(int, input().split()))
count = 0
c = int(input())
for j in range(0, a):
    if (c==b[j]):
        count += 1
print(count)

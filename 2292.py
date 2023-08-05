#2292번 벌집

n = int(input())

a = 1
cnt = 1

while(a<n):
    a += 6*cnt
    cnt += 1

print(cnt)

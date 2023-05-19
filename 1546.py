#1546번 평균

N = int(input())
a = list(map(int, input().split()))
sum = 0

b = max(a)

for i in range(0, N):
    a[i] = a[i]/b*100

for i in range(0, N):
    sum += a[i]

mean = sum/N

print(mean)

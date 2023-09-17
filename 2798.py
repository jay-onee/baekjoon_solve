#2798번 블랙잭

n, m = map(int,input().split())

a = list(map(int, input().split()))
b = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if a[i] + a[j] + a[k] > m:
                continue
            else:
                b = max(b, a[i] + a[j] + a[k])

print(b)

#2501 약수 구하기

n, k = map(int, input().split())
a = []

for i in range(1, n+1):
    if n%i==0:
        a.append(i)

if k>len(a):
    print("0")
else:
    print(a[k-1])
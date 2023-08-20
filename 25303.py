#25305번 커트라인

n, k = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)
a = reversed(a)
a = list(a)
print(a[k-1])

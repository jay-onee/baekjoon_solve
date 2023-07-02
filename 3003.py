#3003번 킹, 퀸, 룩, 비숍, 나이트, 폰

a = list(map(int, input().split()))

piece = [1, 1, 2, 2, 2, 8]

for i in range(len(piece)):
    print(piece[i] - a[i], end=' ')

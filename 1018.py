#1018번 체스판 다시 칠하기

n, m = map(int, input().split())
chess = []
r = []
for _ in range(n):
    chess.append(input())

for i in range(n-7):
    for j in range(m-7):
        w = 0 # 첫번째 흰색
        b = 0 # 첫번째 검정
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if chess[k][l] != "W":
                        w += 1
                    if chess[k][l] != "B":
                        b += 1
                else:
                    if chess[k][l] != "B":
                        w += 1
                    if chess[k][l] != "W":
                        b += 1
        r.append(w)
        r.append(b)
print(min(r))

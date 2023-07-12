#10798번 세로읽기

A = []
B = []

for i in range(0, 5):
    a = input()
    A.append(a)
    
for j in range(0, 15):
    for k in range(0, 5):
        if (j < len(A[k])):
            B.append(A[k][j])

for i in range(0, len(B)):
    print(B[i], end="")

#2566번 최댓값

A = []
B = []

for i in range(0, 9):
    a = list(map(int, input().split()))
    A.append(a)

for j in range(0, 9):
    B.append(max(A[j]))

num = max(B)

for i in range(0, 9):
    for j in range(0, 9):
        if (A[i][j] == num):
            a = i+1
            b = j+1

print(num)
print(a, b)

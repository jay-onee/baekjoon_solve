#11720번 숫자의 합

N = int(input())

x = str(input())
y = 0

for i in range(N):
    y = y + int(x[i])
    
print(y)

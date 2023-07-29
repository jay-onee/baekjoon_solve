#2745번 진법 변환

n, b = map(str, input().split())

num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

b = int(b)
n = n[::-1]
result = 0

for i in range(len(n)):
    result += (b**i)*(num.index(n[i]))

print(result)

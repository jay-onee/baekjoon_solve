#11005번 진법 변환2

n, b = map(int, input().split())

num = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
y = ""
while (n!=0):
    x = n%b
    if (x>=10):
        x -= 9
        x = num[x-1]
        y += str(x)
    else:
        y += str(x)
    n = n//b

y = y[::-1]

print(y)

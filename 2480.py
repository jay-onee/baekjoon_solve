#2480번 주사위 문제

a, b, c = map(int, input().split())

r = 0
m = 0

def Max(a, b, c):
    if (a >= b):
        m = a
    else:
        m = b
    if (m < c):
        m = c
    return m

if (a == b == c):
    r = 10000 + a*1000
elif (a == b and b != c):
    r = 1000 + a*100
elif (b == c and c != a):
    r = 1000 + b*100
elif (c == a and a != b):
    r = 1000 + c*100
else:
    r = Max(a, b, c)*100

print(r)

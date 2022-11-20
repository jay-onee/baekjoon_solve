#2525번 오븐시계

A, B = map(int, input().split()) #A 시간 B 분
C = int(input())

D = C // 60 #몫
E = C % 60 #나머지

if (A + D > 23):
    A = A + D - 24
else:
    A = A + D

if (B + E >= 60):
    B = B + E - 60
    if (A + 1 == 24):
        A = 0
    else:
        A = A + 1
else:
    B = B + E
    

print(A, B)

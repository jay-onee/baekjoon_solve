#2720번 세탁소 사장 동혁

T = int(input())

for i in range (T):
    C = int(input())
    Q = C//25
    R = C-Q*25
    D = R//10
    R = R-D*10
    N = R//5
    R = R-N*5
    P = R

    print(Q, D, N, P)

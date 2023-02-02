#11022번 A+B -8

T = int(input())

for i in range(0, T):
    A, B =  map(int, input().split())
    i_str = str(i + 1)
    sum_str = str(A+B)
    A = str(A)
    B = str(B)
    print("Case #" + i_str + ": " + A + " + " + B + " = " +  sum_str)

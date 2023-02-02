#11021번 A+B -7

T = int(input())

for i in range(0, T):
    A, B =  map(int, input().split())
    i_str = str(i + 1)
    sum_str = str(A+B)
    print("Case #" + i_str + ": " + sum_str)

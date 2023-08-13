#11653번 소인수분해

n = int(input())

a = 2

while (a <= n):
    if (n%a) == 0:
        print(a)
        n = n/a
    else:
        a += 1

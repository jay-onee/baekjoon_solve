#9506번 약수들의 합

while(True):
    n = int(input())
    if (n == -1):
        break;
    a = []
    k = 0
    for i in range(1, n):
        if n%i==0:
            a.append(i)

    for j in range(len(a)):
        k += a[j]

    if (k == n):
        print(n, "=", end=" ")
        print(*a, sep=" + ")
    else:
        print(n, "is NOT perfect.")

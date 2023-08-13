#2581번 소수

m = int(input())
n = int(input())

a = []

for i in range(m, n+1):
    for j in range(2, i+1):
        if i%j == 0:
            if i == j:
                a.append(i)
            break

if (len(a) == 0):
    print("-1")
    
else:
    print(sum(a))
    print(min(a))

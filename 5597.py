#5597 과제 안 내신 분..?

a = []

for i in range(0, 28):
    n = int(input())
    a.append(n)

for j in range(1, 31):
    b = j in a
    if (b==False):
        print(j)

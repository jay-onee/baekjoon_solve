#2587번 대표값2

a = []
sum = 0

for i in range(5):
    b = int(input())
    a.append(b)

a = sorted(a)

for i in range(5):
    sum += a[i]

mean = sum/5

print(round(mean))
print(a[2])

#3052번 나머지

x = []
y = []

for i in range(0, 10):
    a = int(input())
    x.append(a)

for j in range(0, 10):
    tmp = x[j]%42
    if ((tmp in y) == False):
        y.append(tmp)

print(len(y))

#9086번 문자열

T = int(input())

for i in range(T):
    x = str(input())
    y = x[0]+x[len(x)-1]
    print(y)

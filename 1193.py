#1193번 분수찾기

x = int(input())

a = 1

while (x>a):
    x = x-a
    a = a+1

if (a%2==0):
    print(x,"/", a-x+1, sep="")

else:
    print(a-x+1, "/",x , sep="")

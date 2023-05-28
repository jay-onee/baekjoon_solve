#2675번 문자열 반복

T = int(input())

mylist1 = []
mylist2 = []
mylist3 = []

a = ""

for i in range(T):
    R, S = map(str, input().split())
    R = int(R)
    mylist1.append(S)
    mylist3.append(R)

for i in range(T):
    for j in range(len(mylist1[i])):
        for k in range(mylist3[i]):
            a += mylist1[i][j]
    mylist2.append(a)
    a = ""

for i in range(T):
    print(mylist2[i])

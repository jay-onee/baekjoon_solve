#1181번 단어 정렬

n = int(input())

a = []
for _ in range (n):
    a.append(input())
    
a = set(a)
a = list(a)
a.sort()
a.sort(key = len)
for i in range(len(a)):
    print(a[i])

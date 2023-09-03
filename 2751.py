#2751번 수 정렬하기 2
import sys

n = int(input())

a = []

for i in range(n):
    a.append(int(sys.stdin.readline().rstrip()))

a = sorted(a)
for i in range(len(a)):
    print(a[i])

#24267번 알고리즘 수업 - 알고리즘의 수행 시간 6

n = int(input())

sum = 0
a = n-2

for i in range(1, n-1):
    sum += i*a
    a -= 1

print(sum, 3)

#1*(n-2) + 2*(n-3) + ... + (n-2)*1

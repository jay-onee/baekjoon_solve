#2439번 별찍기2

a = int(input())

for i in range(1, a+1):
    print(" " * (a-i) + "*" * i)

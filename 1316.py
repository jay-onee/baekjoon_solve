#1316번 그룹 단어 체커

a = int(input())

for i in range(a):
    b = input()
    for j in range (len(b)-1):
        if b[j] == b[j+1]:
            continue
        elif b[j] in b[j+1:]:
            a -= 1
            break
        
print(a)

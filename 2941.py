#2941번 크로아티아 알파벳

a = input()
count = 0
alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in alphabet:
    a = a.replace(i, "1")
    
print(len(a))

#5622번 다이얼

a = input()

count = 0

for i in range(len(a)):
    if (a[i] == "A" or a[i] == "B" or a[i] == "C"):
        count += 3
    elif (a[i] == "D" or a[i] == "E" or a[i] == "F"):
        count += 4
    elif (a[i] == "G" or a[i] == "H" or a[i] == "I"):
        count += 5
    elif (a[i] == "J" or a[i] == "K" or a[i] == "L"):
        count += 6
    elif (a[i] == "M" or a[i] == "N" or a[i] == "O"):
        count += 7
    elif (a[i] == "P" or a[i] == "Q" or a[i] == "R" or a[i] == "S"):
        count += 8
    elif (a[i] == "T" or a[i] == "U" or a[i] == "V"):
        count += 9
    else:
        count += 10

print(count)

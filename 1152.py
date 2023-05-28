#1152번 단어의 개수

w = str(input())
if w[0] == " ":
    count = 0
else:
    count = 1

for i in range(len(w)-1):
    if (w[i] == " " and w[i+1] != " "):
        count += 1

print(count)

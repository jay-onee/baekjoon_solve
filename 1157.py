#1157번 단어공부

a = input().upper()

a_list = list(set(a))

count_list = []

b = 0
for i in (a_list):
    cnt = a.count(i)
    count_list.append(cnt)

num = count_list.index(max(count_list))

for j in (count_list):
    b = count_list.count(max(count_list))

if (b > 1):
    print("?")
else:
    print(a_list[num])

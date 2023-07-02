#10988번 팰린드롬인지 확인하기

word = input()

tmp = word[::-1]

if (word == tmp):
    print("1")
else:
    print("0")

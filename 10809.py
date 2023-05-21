#10809번 알파벳 찾기

s = str(input())

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if i in s:
        print(s.index(i), end = ' ')
    else:
        print(-1, end = ' ')

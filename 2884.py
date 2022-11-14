#2884번 알람시계

H, M = map(int, input().split())
if (H != 0 and M < 45):
    H -= 1
    M = abs(60 - (45 - M))
elif (H == 0 and M < 45):
    H = 23
    M = abs(60 - (45 - M))
elif (M >= 45):
    M -= 45

print(H, M)

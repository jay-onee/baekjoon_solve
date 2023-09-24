#25206번 너의 평점은

credit = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

a = []
d = []
for _ in range(20):
    s, c, g = input().split()
    c = float(c)
    if g != "P":
        b = grade[(credit.index(g))] * c
        a.append(b)
        d.append(c)
    if sum(d) != 0:
        result = sum(a)/sum(d)

print('%.6f' % result)

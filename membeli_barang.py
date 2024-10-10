m, n = map(int, input().split())

p = list(map(int, input().split()))[:m]

c = list(map(int, input().split()))[:n]


p1 = []
p2 = []
for i in p:
    if i < 0:
        p2.append(i)
        if p2 == p:
            p1.append(max(p))
            break

for i in p:
    if i > 0:
        p1.append(i)


c1 = []
c2 = []
for j in c:
    if j > 0:
        c2.append(j)
        if c2 == c:
            c1.append(min(c))
            break

for j in c:
    if j < 0:
        c1.append(j)


harga = sum(p1)
uang = sum(c1)
bayar = uang - harga

print(bayar)

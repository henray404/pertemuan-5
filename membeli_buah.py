N, K = map(int, input().split())
Ai = list(map(int, input().split()))

buah = 0
jenis = []
for i in range(len(Ai)):
    if Ai[i] <= K:
        buah += 1
        jenis.append(i+1)

angka_buah = ""
for i in jenis:
    if i != jenis[-1]:
        angka_buah += f"jenis ke {i}, "
    else:
        angka_buah += f"dan jenis ke {i}"
        break

print(
    f"dengan uang {K} ia bisa membeli dengan kemungkinan {buah} jenis buah yaitu buah {angka_buah}")
print(buah)

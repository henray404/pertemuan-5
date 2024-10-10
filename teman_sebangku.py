N, R, C = map(int, input().split())
position = {}
for i in range(N):
    x, a, b = list(map(int, input().split()))
    position[(a, b)] = x

for i in range(1, N+1):
    non = True
    for (a, b), student in position.items():
        if student == i:
            if (a, b-1) in position:
                print(position[(a, b-1)])
                non = False
            elif (a, b+1) in position:
                print(position[(a, b+1)])
                non = False
            break

    if non:
        print(0)

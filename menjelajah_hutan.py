R, C, N = map(int, input().split())


maps = [list(map(int, input().split())) for i in range(R)]


movement = input()

x, y = 0, 0

move_direction = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)

}

gold = 0
nabrak = False

for i in movement:

    dx, dy = move_direction[i]
    nx, ny = x + dx, y + dy

    if 0 <= nx < R and 0 <= ny < C:
        position = int(maps[nx][ny])
        gold += int(position)

        if i == "U" or i == "R":
            gold += 3

        elif i == "D" or i == "L":
            gold -= 2

    else:
        nabrak = True
        break

    x, y = nx, ny
    print(gold, i)

print(gold)

if nabrak:
    print("gerakanmu salah bung!")

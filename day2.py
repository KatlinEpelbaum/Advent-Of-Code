f = open("input.txt")

lines = f.readlines()

res = 0

for line in lines:
    line_splitted = line.split (":")
    game_id = int(line_splitted[0].split()[1])
    is_possible = True

    for round in line_splitted[1].split(";"):
        for color in round.split(","):
            nr, cn = color.split()
            nr = int(nr)

            if not (cn == "red" and nr <= 12 or cn == "blue" and nr <= 14 or cn == "green" and nr <= 13):
                  is_possible = False

    print(is_possible, game_id)
    if is_possible == True:
        res += game_id

print("The sum of the game IDs is", res)

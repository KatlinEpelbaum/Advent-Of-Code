f = open("example.txt")

lines = f.readlines()

for line in lines:
    line_splitted = line.split (":")
    game_id = int(line_splitted[0].split()[1])

    for round in line_splitted[1].split(";"):
        print(round)


    print()


# print(lines)
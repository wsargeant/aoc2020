with open("day_1.txt") as f:
    #number_list = list(map(int, (f.read()).split("\n")))
    number_list = [int(x) for x in f.read().split("\n")]
    matches = [(x,y) for x in number_list for y in number_list if x+y == 2020]
    print(matches[0][0] * matches[0][1])

    part_2_matches = [(x,y,z) for x in number_list for y in number_list for z in number_list if x+y+z == 2020]
    print(part_2_matches[0][0] * part_2_matches[0][1] * part_2_matches[0][2])
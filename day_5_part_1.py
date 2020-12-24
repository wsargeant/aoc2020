# import itertools

# rows = ["F","F","F","F","F","F","F","B","B","B","B","B","B","B"]
# columns = ["L", "R"]

# d = list(itertools.permutations(rows, 7))
# e = list(itertools.combinations_with_replacement(columns, 3))
# print(d)
# print(e)

F_count = 0
B_count = 0

with open("day_5.txt") as f:
    boarding_passes = f.read().split("\n")
    boarding_passes.sort()
    for i in boarding_passes:
        print(i)
    # for i in range(7):
    #     for seat in boarding_passes:
    #         if seat[i] == "F":
    #             F_count += 1
    #         if seat[i] == "B":
    #             B_count += 1
    #     if F_count < B_count:
    #         print("F")
    #     else:
    #         print("B")

#print(F_count, B_count)

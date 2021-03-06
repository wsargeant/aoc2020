def boardingpass_converter(boardingpass):
    binary_boarding_pass = boardingpass.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    row = int(binary_boarding_pass[:7], 2)
    column = int(binary_boarding_pass[7:], 2)
    seat_number = row * 8 + column
    return seat_number

with open("day_5.txt") as f:
    boardingpasses = [x.strip() for x in f.readlines()]
    seats = [boardingpass_converter(x) for x in boardingpasses]
    print (max(seats)
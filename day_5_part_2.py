import timeit

def boardingpass_converter(boardingpass):
    binary_boarding_pass = boardingpass.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    row = int(binary_boarding_pass[:7], 2)
    column = int(binary_boarding_pass[7:], 2)
    seat_number = row * 8 + column
    return seat_number

def slow_find_seats(seats):
    for i in range(min(seats), max(seats)):
        if i not in seats:
            return i

def fast_find_seats(seats):
    seats_set = set(seats)
    for i in range(min(seats), max(seats)):
        if i not in seats_set:
            return i


with open("day_5.txt") as f:
    boardingpasses = [x.strip() for x in f.readlines()]
    seats = [boardingpass_converter(x) for x in boardingpasses]

    print(timeit.timeit(lambda: fast_find_seats(seats), number=10000)/10000)
    print(timeit.timeit(lambda: slow_find_seats(seats), number=10000)/10000)
    

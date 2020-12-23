def read_integers(filename):
    """ Returns list of numbers from file containing list of numbers separated by new lines
    """
    infile = open(filename, "r")
    number_list = []
    while True:
        num = infile.readline()
        if len(num) == 0:
            break
        if "\n" in num:
            num = num[:-1]
        number_list.append(int(num))

    return(number_list)

def sum_2020(filename):
    """Returns two numbers from number list in filename which sum to 2020 and their product
    """
    number_list = read_integers(filename)
    matches = [(x,y) for x in number_list for y in number_list if x+y == 2020]
    return matches[0][0] * matches[0][1]


def sum_2020_by_3(filename):
    """Returns three numbers from number list in filename which sum to 2020 and their product
    """
    number_list = read_integers(filename)
    matches = [(x,y,z) for x in number_list for y in number_list for z in number_list if x+y+z == 2020]   
    return matches[0][0] * matches[0][1] * matches [0][2] 

print(sum_2020("day_1.txt"))

print(sum_2020_by_3("day_1.txt"))
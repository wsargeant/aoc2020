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
    target = 2020
    matches = [(x,y) for x in number_list for y in number_list if x+y == 2020]
    """
    for num1 in number_list:
        num2 = target - num1
        if num2 in number_list and num2 != num1:
            break
    return num1, num2, num1*num2
    """
    return matches


def sum_2020_by_3(filename):
    """Returns three numbers from number list in filename which sum to 2020 and their product
    """
    number_list = read_integers(filename)
    #reversed_number_list = number_list.copy()
    #reversed_number_list.reverse()
    target = 2020
    matches = [(x,y,z) for x in number_list for y in number_list for z in number_list if x+y+z == 2020]
    for x in number_list:
        for y in number_list:
            for z in number_list:
                if x+ y + z == 2020:
                    return x*y*z
    """
    for i in range(len(number_list)):
        num1 = number_list[i]
        for j in range(i,len(number_list)):
            num2 = number_list[j]
            num3 = target - num1 - num2
            if num3 >= 0 and num3 in number_list:
                return num1, num2, num3, num1*num2*num3
    return False
    """
    return matches 

print(sum_2020("day_1.txt"))

print(sum_2020_by_3("day_1.txt"))
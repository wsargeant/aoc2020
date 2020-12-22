def read_password_list(filename):
    """ Returns number of passwords which contain the specified character in a number within the upper and lower limits
    """
    password_count = 0
    infile = open(filename, "r")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if "\n" in text:
            text = text[:-1]
    
        text = text.split()
        limits = text[0].split("-")
        lower_limit = int(limits[0])
        upper_limit = int(limits[1])
        character = text[1][0]
        password = text[2]

        character_count = 0

        for i in password:
            if i == character:
                character_count += 1

        
        if lower_limit <= character_count <= upper_limit:
            password_count += 1

    return password_count

def read_password_list_2(filename):
    """ Returns number of passwords contain the character in 
    only 1 of the two specified index positions (neglecting index 0)
    """
    password_count = 0
    infile = open(filename, "r")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if "\n" in text:
            text = text[:-1]
    
        text = text.split()
        indexes = text[0].split("-")
        lower_index = int(indexes[0]) - 1
        upper_index = int(indexes[1]) - 1
        character = text[1][0]
        password = text[2]


        if (password[lower_index] == character and password[upper_index] != character) or (password[lower_index] != character and password[upper_index] == character):
            password_count += 1

    return password_count

print(read_password_list("day_2.txt"))

print(read_password_list_2("day_2.txt"))

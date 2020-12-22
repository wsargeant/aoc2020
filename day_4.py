def get_credentials_list(filename):
    infile = open(filename, "r")
    current_credentials = []
    all_credentials = []
    while True:
        contents = infile.readline()
        if len(contents) == 0:
            break
        if "\n" in contents:
            contents = contents[:-1]
        if len(contents) != 0:
            contents = contents.split(" ")
            current_credentials.append(contents)
        if len(contents) == 0:
            current_credentials = sum(current_credentials, [])
            current_credentials.sort()
            #print(current_credentials)
            all_credentials.append(current_credentials)
            current_credentials = []

    #all_credentials.sort()
    #print(all_credentials)
    #print(len(all_credentials))
    return all_credentials

def credentials_check(filename, required_credentials_list):
    valid_passport_count = 0
    #invalid_passport_count = 0
    required_num_creds = len(required_credentials_list)
    all_credentials = get_credentials_list(filename)

    #for passport in all_credentials:
    #    cred_count = 0
    #    for field in passport:
    #        field = field[:3]
    #        for cred in required_credentials_list:
    #            if field.find(cred) != -1:
    #                cred_count +=1
    #    if cred_count == required_num_creds:
    #        valid_passport_count += 1
    
    for passport in all_credentials:
        for field in passport:
            field = field[:3]
            if "cid" in field:
                if len(passport) == len(required_credentials_list) + 1:
                    valid_passport_count += 1

        if len(passport) == len(required_credentials_list):
            valid_passport_count += 1
    
    return valid_passport_count

"""
def credentials_checker(filename, required_credentials_list, optional_credentials_list):
    all_credentials = get_credentials_list(filename) # get a list of lists where each sublist is the credentials of one passport
    required_credentials_list.sort() # sort the list of reqiured credentials
    optional_credentials_list.sort() #sort the list of optional credentials
    cred_count = 0 # count of required credentials found
    valid_passport_count = 0 # count of valid passports found
    for passport in all_credentials:
        for field in passport:
            field = field[:3] # remove the details after each field key (in case any details contain strings matching the field abbreviations)
            for cred in required_credentials_list:
                if field.find(cred) == -1:
                    print(field)
                    for opt_cred in optional_credentials_list:
                        if field.find(opt_cred) == -1:
                            break
                if field.find(cred) != -1:
                    cred_count += 1
                    required_credentials_list = required_credentials_list[1:]
                if cred_count == len(required_credentials_list):
                    valid_passport_count += 1
                    break               
        
    
    return valid_passport_count

    """

print(get_credentials_list("day_4.txt"))

required_credentials_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_credentials_list = ["cid"]

print(credentials_check("day_4.txt", required_credentials_list))
# print(credentials_checker("day_4.txt", required_credentials_list, optional_credentials_list))

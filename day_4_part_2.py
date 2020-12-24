import re

def make_year_validator(startyear, endyear):
    def year_validator(year):
        try:
            return startyear <= int(year) <= endyear
        except (ValueError, TypeError):
            return False
    return year_validator

def make_height_validator(metric_min, metric_max, imperial_min, imperial_max):
    def height_validator(height): 
        if height == None:
            return False
        if "cm" in height:
            try:
                return metric_min <= int(height[:-2]) <= metric_max
            except (ValueError, TypeError):
                return False
        if "in" in height:
            try:
                return imperial_min <= int(height[:-2]) <= imperial_max
            except (ValueError, TypeError):
                return False
        else:
            return False
    return height_validator

def hair_colour_validator(haircolour):
    try:
        return re.fullmatch(r"#[\da-f]{6}", haircolour) is not None
        #return re.match(r"^#[\da-f]{6}$", haircolour) is not None 
    except TypeError:
        return False

def make_eye_colour_validator(allowed_eyecolour_list):
    def eye_colour_validator(eyecolour):
        return eyecolour in allowed_eyecolour_list
    return eye_colour_validator

def passport_id_validator(id_number):
    try:
        return re.fullmatch(r"[\d]{9}", id_number) is not None
    except TypeError:
        return False

def passport_to_dict(passport):
    passport_fields = passport.split()
    split_fields = [x.split(":") for x in passport_fields]
    return { s[0]: s[1] for s in split_fields}

def passport_is_valid(required, passport):
    passport_dict = passport_to_dict(passport)
    return all([validator(passport_dict.get(field)) for (field, validator) in required.items()])

with open("day_4.txt") as f:
    passports = f.read().split("\n\n")
    required = {"byr": make_year_validator(1920, 2002), "iyr": make_year_validator(2010, 2020), "eyr": make_year_validator(2020, 2030), "hgt": make_height_validator(150, 193, 59, 76), "ecl": make_eye_colour_validator(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]), "hcl": hair_colour_validator , "pid": passport_id_validator}
    valid_passports_count = len([1 for passport in passports if passport_is_valid(required, passport) ])
    print (valid_passports_count)
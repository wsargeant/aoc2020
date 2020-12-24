def are_fields_present(required, passport):
   passport_fields = passport.split()
   actual_fields = [x[:3] for x in passport_fields]
   for r in required:
      if r not in actual_fields:
        return False
   return True

with open("day_4.txt") as f:
   passports = f.read().split("\n\n")
   required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
   valid_passports_count = len([1 for passport in passports if are_fields_present(required, passport) ])
   print (valid_passports_count)
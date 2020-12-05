#####################################################################
#                                                                   #
#   Name: AOC_Day04.py                                              #
#                                                                   #
#   Author: Titouan "Dr_LuX" Allain                                 #
#   Date created: 04/12/20 00:40                                    #
#   Last modification: 05/12/20 18:12                               #
#                                                                   #
#####################################################################

import string

pass_valid = 0
# Eye Color condition
list_ecl =  ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
# Passport's argument
list_pass=["byr","iyr","eyr","hgt","hcl","ecl","pid"]

with open("data4.txt","r") as f:
    lines = f.read().splitlines()
    arg_valid = 0
    for line in lines:
        # If we have an empty line, so we're looking for another passport
        if line == '':
            arg_valid = 0
        line = line.split(' ')
        for arg in line:
            arg = arg.split(':')
            if arg[0] in list_pass:
                # Birth Year case
                if arg[0] == "byr":
                    if int(arg[1]) >= 1920 and int(arg[1]) <= 2002:
                        arg_valid += 1
                # Issue Year case
                if arg[0] == "iyr":
                    if int(arg[1]) >= 2010 and int(arg[1]) <= 2020:
                        arg_valid += 1
                # Expiration Year case
                if arg[0] == "eyr":
                    if int(arg[1]) >= 2020 and int(arg[1]) <= 2030:
                        arg_valid += 1
                # Height case
                if arg[0] == "hgt":
                    nbstr = ""
                    # inch case (xxin)
                    if len(arg[1]) == 4:
                        if arg[1][2] == 'i' and arg[1][3] == 'n':
                            # copy the 2 digits to a string for check the condition
                            nbstr += arg[1][0]
                            nbstr += arg[1][1]
                            if int(nbstr) >= 59 and int(nbstr) <= 76:
                                arg_valid += 1
                    # centimeter case (xxxcm)
                    if len(arg[1]) == 5:
                        if arg[1][3] == 'c' and arg[1][4] == 'm':
                            # copy the 3 digits to a string for check the condition
                            nbstr += arg[1][0]
                            nbstr += arg[1][1]
                            nbstr += arg[1][2]
                            if int(nbstr) >= 150 and int(nbstr) <= 193:
                                arg_valid += 1
                # Hair Color case
                if arg[0] == "hcl":
                    # verify is an hex value
                    if len(arg[1]) == 7:
                        nb_hcl = 0
                        if arg[1][0] == "#":
                            for i in range(1, 7):
                                if arg[1][i] in string.hexdigits:
                                    nb_hcl += 1
                            if nb_hcl == 6:        
                                arg_valid += 1
                # Eye Color case
                if arg[0] == "ecl":
                    if arg[1] in list_ecl:
                        arg_valid += 1
                # Passport ID case   
                if arg[0] == 'pid':
                    # verify if they're 9 digits
                    if len(arg[1]) == 9:
                        if arg[1].isnumeric:
                            arg_valid += 1
        # verify we got all 7 args for validate passport
        if arg_valid == 7:
            pass_valid += 1
            arg_valid = 0
print(pass_valid)
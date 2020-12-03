#####################################################################
#                                                                   #
#   Name: AOC_Day02.py                                              #
#                                                                   #
#   Author: Titouan "Dr_LuX" Allain                                 #
#   Date created: 02/12/20                                          #
#   Last modification: 04/12/20 00:24                               #
#                                                                   #
#####################################################################


with open("data2.txt","r") as f:
    valid = 0
    lines = f.readlines()
    for line in lines:        
        line_list = line.split(' ')
        nbs = line_list[0].split('-')
        mini = nbs[0]
        maxi = nbs[1]
        letter = line_list[1].replace(":","")
        pwd = line_list[2]
        if pwd[int(mini)-1] == letter and pwd[int(maxi)-1] != letter or pwd[int(mini)-1] != letter and pwd[int(maxi)-1] == letter:
            valid += 1 
print("{}".format(valid))
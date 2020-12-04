#####################################################################
#                                                                   #
#   Name: AOC_Day02.py                                              #
#                                                                   #
#   Author: Titouan "Dr_LuX" Allain                                 #
#   Date created: 03/12/20                                          #
#   Last modification: 04/12/20 10:28                               #
#                                                                   #
#####################################################################

result = 0
for time in range(5):
    if time == 0:
        mod_col = 1
    elif time == 1:
        mod_col = 3
    elif time == 2:
        mod_col = 5
    elif time == 3:
        mod_col = 7
    elif time == 4:
        mod_col = 1
    with open("data3.txt","r") as f:
        count = 0
        num_line = 1
        pos_col = 0
        line = f.readline()
        while num_line < 323:
            if time == 4:
                line = f.readline()
                num_line += 1
            pos_col += mod_col        
            if pos_col >= len(line)-1:
                pos_col -= 31
            line = f.readline()
            num_line += 1
            if line[pos_col] == '#':
                count += 1
    if result == 0:
        result = count
    else:
        result *= count
print(result)

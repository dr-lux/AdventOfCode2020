#####################################################################
#                                                                   #
#   Name: AOC_Day12.py                                              #
#                                                                   #
#   Author: Titouan "Dr_LuX" Allain                                 #
#   Date created: 14/12/20 15:36                                    #
#   Last modification: 11/12/20 12:19                               #                                        
#                                                                   #
#####################################################################

def main():
    honrizontal_value = 0
    vertical_value = 0
    rotation = 0


    # with open(".txt","r") as f:
    with open("a.txt","r") as f:
        lines = f.read().splitlines()
        for line in lines:
            line_value = int(line[1:])
            # print(line_value)
            if line[0] == "F":
                if rotation == 0:
                    honrizontal_value += line_value
                elif rotation == 90: 
                    vertical_value -= line_value
                elif rotation == 180:
                    honrizontal_value -= line_value
                else:
                    vertical_value += line_value
            elif line[0] == "R":
                rotation += line_value
                if rotation > 270:
                    rotation -= 270
            elif line[0] == "L":
                rotation -= line_value
                if rotation < 0:
                    rotation += 270
            elif line[0] == "N":
                vertical_value += line_value
            elif line[0] == "E":
                honrizontal_value += line_value
            elif line[0] == "S":
                vertical_value -= line_value
            else:
                vertical_value -= line_value
    
    print(honrizontal_value)
    print(vertical_value)


if __name__ == "__main__":
    main()
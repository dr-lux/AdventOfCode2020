#####################################################################
#                                                                   #
#   Name: AOC_Day11.py                                              #
#                                                                   #
#   Author: Titouan "Dr_LuX" Allain                                 #
#   Date created: 11/12/20 00:14                                    #
#   Last modification: 11/12/20 12:19                               #                                        
#                                                                   #
#####################################################################

def main():
    seats_list = list()
    new_list = list()
    modification = True

    # with open("data10.txt","r") as f:
    with open("t.txt","r") as f:
    # with open("a.txt","r") as f:
        lines = f.read().splitlines()
        for line in lines:
            row_list = list()
            new_row_list = list()
            for column in line:
                if column == "L":
                    row_list.append("#")
                    new_row_list.append("#")
                else:
                    row_list.append(column)
                    new_row_list.append(column)
            seats_list.append(row_list)
            new_list.append(new_row_list)

    # new_list = [[None] * len(seats_list[0])] * len(seats_list)
    
    for row in range(len(seats_list)-1):
            for column in range(len(seats_list[row])-1):
                # print(seats_list[row][column])
                new_list[row][column] = seats_list[row][column]
                # print(seats_list[row][column])
    # print(seats_list)
    # print(new_list)
    while(modification):
        modification = False


                

        for row in range(len(seats_list)-1):
            for column in range(len(seats_list[row])-1):
                # print(seats_list)
                filled_neighbor_seat = 0
                # print(seats_list[row][column])
                # print("LEN",len(seats_list[row]))
                # print("\n",seats_list[row][column])    
                # print("row",row)
                # print("column",column)
                if seats_list[row][column] == "#": # be opti
                    if row == 0 and column == 0 or row == len(seats_list)-1 and column == 0 or row == 0 and column == len(seats_list[row])-1 or row == len(seats_list)-1 and column == len(seats_list[row])-1:
                        continue
                    elif row == 0:
                        # print("behind",seats_list[row][column - 1])
                        if seats_list[row][column - 1] == "#":
                            filled_neighbor_seat += 1
                        # print("after",seats_list[row][column + 1])
                        if seats_list[row][column + 1] == "#":
                            filled_neighbor_seat += 1
                        for check_column in range(-1,2):
                            # print("nextrow",seats_list[row + 1][column - check_column])
                            if seats_list[row + 1][column - check_column] == "#":
                                filled_neighbor_seat += 1
                        # if filled_neighbor_seat >= 4:
                            # seats_list[row][column] = "L"
                    elif row == len(seats_list)-1:
                        if seats_list[row][column - 1] == "#":
                            filled_neighbor_seat += 1
                        if seats_list[row][column + 1] == "#":
                            filled_neighbor_seat += 1
                        for check_column in range(-1,2):
                            if seats_list[row - 1][column - check_column] == "#":
                                filled_neighbor_seat += 1
                    
                    elif column == 0:
                        if seats_list[row - 1][column] == "#":
                            filled_neighbor_seat += 1
                        if seats_list[row + 1][column] == "#":
                            filled_neighbor_seat += 1
                        for check_row in range(-1,2):
                            if seats_list[row - check_row][column + 1] == "#":
                                filled_neighbor_seat += 1
                    
                    elif column == len(seats_list[row])-1:
                        if seats_list[row - 1][column] == "#":
                            filled_neighbor_seat += 1
                        if seats_list[row + 1][column] == "#":
                            filled_neighbor_seat += 1
                        for check_row in range(-1,2):
                            if seats_list[row - check_row][column - 1] == "#":
                                filled_neighbor_seat += 1
                    
                    else:
                        for check_row in range (-1,2):
                            for check_column in range (-1,2):
                                if check_row == 0 and check_column == 0:
                                    continue
                                elif seats_list[row - check_row][column - check_column] == "#":
                                    filled_neighbor_seat += 1
                    

                    # print("Nei",filled_neighbor_seat)
                    if filled_neighbor_seat >= 4:
                    
                        new_list[row][column] = "L"
                        # modification = True

        # for row in range(len(seats_list)):
            # for column in range(len(seats_list[row])):
                # seats_list[row][column] = new_seats_list[row][column]
    
    print(new_list)
    




if __name__ == "__main__":
    main()
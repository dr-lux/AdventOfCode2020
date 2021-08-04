#####################################################################
#                                                                   #
#   Name: AOC_Day10.py                                              #
#                                                                   #
#   Author: Titouan "Dr_LuX" Allain                                 #
#   Date created: 09/12/20 22:24                                    #
#   Last modification: 10/12/20 12:19                               #                                        
#                                                                   #
#####################################################################

def check_list(num_list,arr,pos_to_remove):
    removed = num_list[pos_to_remove]
    del num_list[pos_to_remove]
    for pos in range(len(num_list)-1):
        if (num_list[pos+1]-num_list[pos] == 1 or num_list[pos+1]-num_list[pos] == 3):
            continue
        else:
            break
    else:
        print(num_list)
        if len(num_list) > pos_to_remove:
            arr += check_list(num_list,arr,pos_to_remove)
        num_list.append(removed)
        num_list.sort()
        return(1)
    # print("AFTER",num_list)
    return(0)


def main():
    num_list = list()
    sorted_num_list = list()
    highest_rated = 0
    one = 0
    three = 0
    pos = 0
    arr = 1
    way_num_value = list()

    num_list.append(0)
    with open("data10.txt","r") as f:
    # with open("t.txt","r") as f:
        lines = f.read().splitlines()
        # Copy values in a list
        for line in lines:
            num_list.append(int(line))
    num_list.sort()
    highest_rated = num_list[-1] + 3
    num_list.append(highest_rated)
    while (pos < len(num_list)-1):
        if (num_list[pos+1]-num_list[pos] == 1):
            one += 1
        else:
            three += 1
        pos += 1
    print("O",one)
    print("T",three)
    # Count the number of distinct ways possible
    for num in num_list:
        # print(num)
        if num == 0:
            way_num_value.append(1)
        else:
            way_to_this_value = 0
            # print("DEBUG")
            # print(num_list[num_list.index(num)] - 3)
            # print(num_list[num_list.index(num)] - 2)
            # print(num_list[num_list.index(num)] - 1)
            # print("ENDDEB")
            if num_list[num_list.index(num)] - 3 in num_list:
                # print("-3val",way_num_value[num_list.index(num_list[pos]-3)])
                way_to_this_value += way_num_value[num_list.index(num_list[num_list.index(num)]-3)]
            if num_list[num_list.index(num)] - 2 in num_list:
                # print("-2val",way_num_value[num_list.index(num_list[pos]-2)])
                way_to_this_value += way_num_value[num_list.index(num_list[num_list.index(num)]-2)]
            if num_list[num_list.index(num)] - 1 in num_list:
                # print("-1val",way_num_value[num_list.index(num_list[pos]-1)])
                way_to_this_value += way_num_value[num_list.index(num_list[num_list.index(num)]-1)]
            way_num_value.append(way_to_this_value)
            # print(way_to_this_value)
            # way_num_value[num_list.index(num)] = way_num_value[num_list.index(num)-1] + way_num_value[num_list.index(num)-2] + way_num_value[num_list.index(num)-3]

    # pos = 0
    # num_list.append(highest_rated)
    # while (pos < len(num_list)):
    #     if (num_list[pos] == 1):
    #         way_num_value.append(1)
    #     else:

    #         # print("Num",num_list[pos])
    #         # way_to_this_value = 0
    #         # if num_list[pos] - 3 in num_list:
    #         #     # print("-3val",way_num_value[num_list.index(num_list[pos]-3)])
    #         #     way_to_this_value += way_num_value[num_list.index(num_list[pos]-3)]
    #         # if num_list[pos] - 2 in num_list:
    #         #     # print("-2val",way_num_value[num_list.index(num_list[pos]-2)])
    #         #     way_to_this_value += way_num_value[num_list.index(num_list[pos]-2)]
    #         # if num_list[pos] - 1 in num_list:
    #         #     # print("-1val",way_num_value[num_list.index(num_list[pos]-1)])
    #         #     way_to_this_value += way_num_value[num_list.index(num_list[pos]-1)]
    #         # way_num_value.append(way_to_this_value)
    #         # print("WAY",way_to_this_value)
    #     pos += 1
    # print(way_num_value)
    print(way_num_value[-1])

if __name__ == "__main__":
    main()
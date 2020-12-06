#####################################################################
#                                                                   #
#   Name: AOC_Day05.py                                              #
#                                                                   #
#   Author: Titouan "Dr_LuX" Allain                                 #
#   Date created: 04/12/20 00:52                                    #
#   Last modification: 06/12/20 17:20                               #
#                                                                   #
#####################################################################

max_id = 0
ids_list = list()

with open("data5.txt","r") as f:
    lines = f.read().splitlines()
    # Max ID identification
    for line in lines:
        # Row position
        min = 0
        max = 127
        for pos in range(7):
            div = int((max-min)/2)
            # Lower half case
            if line[pos] == 'F':
                max = max-div-1
                row = max
            # Upper half case
            else:
                min = min+div+1
                row = min
        # Column position
        min = 0
        max = 7
        for pos in range (7,10):
            div = int((max-min)/2)
            # Lower half case
            if line[pos] == 'L':
                max = max-div-1
                col = max
            # Upper half case
            else:
                min = min+div+1
                col = min
        id = row*8+col
        if id > max_id:
            max_id = id
        ids_list.append(id)
    print("The max ID is {}".format(max_id))
    # Sort ID and mark them
    ids_sorted_list = ["None"] * (max_id + 1)
    for id in ids_list:
        ids_sorted_list[id] = 'X'
    # Find the unmarked ID, so the empty place
    for id in range(1,max_id):
        if ids_sorted_list[id] == "None" and ids_sorted_list[id-1] != "None" and ids_sorted_list[id+1] != "None":
            print("The empty place is on ID {}".format(id))

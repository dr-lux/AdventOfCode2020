#####################################################################
#                                                                   #
#   Name: AOC_Day09.py                                              #
#                                                                   #
#   Author: Titouan "Dr_LuX" Allain                                 #
#   Date created: 08/12/20 20:46                                    #
#   Last modification: 09/12/20 12:19                               #                                        
#                                                                   #
#####################################################################

def find_not_right_property_number(num_list):
    pos = 0
    preambule_size = 25
    preambule_list = list()

    while(pos != len(num_list)):
            found = False
            # Check with only preambule list statement
            if pos > preambule_size:
                preambule_list.pop(0)
                # Find the first term loop       
                for first_term in preambule_list:
                    # Find the second term loop
                    for second_term in preambule_list:
                        # Terms found statement
                        if first_term and second_term and first_term != second_term and first_term + second_term == num_list[pos]:
                            preambule_list.append(num_list[pos])
                            found = True
                            break
                    else:
                        continue
                    break
            # Check with 0 to 25 and the begin of preambule list statement
            else:
                # Find the first term loop
                for i in range(25):
                    # Find the second term with 0 to 24 loop
                    for j in range(24):
                        # Terms found statement
                        if i != j and i + j == num_list[pos]:
                            preambule_list.append(num_list[pos])
                            found = True
                            break
                    else:
                        # Find the second term with preambule list
                        for j in preambule_list:
                            if i != j and i + j == num_list[pos]:
                                preambule_list.append(num_list[pos])
                                found = True
                                break
                        continue
                    break
            # Terms not found statetement
            if found == False:
                not_right_property_number = num_list[pos]
                break
            pos += 1
    return(not_right_property_number)

def find_encryption_weakness_number(num_list,not_right_property_number):
    pos = 0
    sum_list = list()

    # Find the contiguous set that sum is the number does not have the right property loop
    while(pos != len(num_list)):
        # Sum of the contiguous set too small statement
        if sum(sum_list) < not_right_property_number:
            sum_list.append(int(num_list[pos]))
            pos += 1
        # Sum of the contiguous set too big statement
        elif sum(sum_list) > not_right_property_number:
            del sum_list[0]
        # Contiguous set found statement
        else:
            break
    sum_list.sort()
    return (sum_list[0]+sum_list[-1])

def main():
    num_list = list()

    with open("data9.txt","r") as f:
        lines = f.read().splitlines()
        # Copy values in a list
        for line in lines:
            num_list.append(int(line))
    # Find the first number that does not have the right property
    not_right_property_number = find_not_right_property_number(num_list)
    # Find the encryption weakness number
    encryption_weakness_number = find_encryption_weakness_number(num_list,not_right_property_number)
    print("The first number that does not have the right property is {}.".format(not_right_property_number))
    print("The encryption weakness number is {}.".format(encryption_weakness_number))


if __name__ == "__main__":
    main()
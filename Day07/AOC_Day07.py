#####################################################################
#                                                                   #
#   Name: AOC_Day07.py                                              #
#                                                                   #
#   Author: Titouan "Dr_LuX" Allain                                 #
#   Date created: 07/12/20 05:57                                    #
#   Last modification: 07/12/20 21:57                               #
#                                                                   #
#####################################################################

def count_bag(lines,color_to_find):
    nb_bag = 0
    for line in lines:
        splited_line = line.split(" ")
        # Fetch line of the corresponding color to find
        if splited_line[0] + " " + splited_line[1] == color_to_find:
            # Calculate number of bag who contain them
            for indice_line in range(len(splited_line)):
                if (splited_line[indice_line]).isnumeric():
                    nb_bag += int(splited_line[indice_line])+int(splited_line[indice_line])*count_bag(lines,splited_line[indice_line+1]+" "+splited_line[indice_line+2])
    return(nb_bag)

def main():
    color_list = ["shiny gold"]
    color_to_find = "shiny gold"
    nb_bag = 0

    with open("data7.txt","r") as f:
        lines = f.read().splitlines()
        # Find bag who contain at least one shiny gold bag
        for color in color_list:
            for line in lines:
                if color in line:
                    line_elm = line.split(" ")
                    # Add the unlisted color who contain shiny gold color or a color who contain this one
                    if line_elm[0] + " " + line_elm[1] not in color_list:
                        color_list.append(line_elm[0] + " " + line_elm[1]) 
        # Launch recursive function to count how many bag they're in a shiny bag
        nb_bag = count_bag(lines,color_to_find)

    # Remove this element because we don't need to count this one
    color_list.remove("shiny gold")

    # Display results
    print("They're {} bags colors can eventually contain at least one shiny gold bag".format(len(color_list)))
    print("They're {} bags inside a single shiny gold bag.".format(nb_bag))

if __name__ == "__main__":
    main()
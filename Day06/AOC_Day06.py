#####################################################################
#                                                                   #
#   Name: AOC_Day06.py                                              #
#                                                                   #
#   Author: Titouan "Dr_LuX" Allain                                 #
#   Date created: 06/12/20 01:38                                    #
#   Last modification: 06/12/20 19:24                               #
#                                                                   #
#####################################################################

all_questions = list()
first_questions = list()
remains_questions = list()
nb_question = 0
yes = 0
deb = 1

with open("data6.txt","r") as f:
    lines = f.read().splitlines()
    for line in lines:
        # New group's answers case
        if line == '':
            yes += len(remains_questions)
            nb_question += len(all_questions)
            all_questions = list()
            first_questions = list()
            remains_questions = list()
            deb = 1
            continue
        # First answer case
        if deb == 1:
            for pos in range(len(line)):
                all_questions.append(line[pos])
                first_questions.append(line[pos])
                remains_questions.append(line[pos])
        # Other case
        else:
            for pos in range(len(line)):
                if line[pos] not in all_questions:
                    all_questions.append(line[pos])
            for elm in first_questions:
                if elm not in line and elm in remains_questions:
                    remains_questions.remove(elm)
        if deb == 1:
            deb = 0
    # After the last line
    yes += len(remains_questions)
    nb_question += len(all_questions)
print("Number of questions to which anyone answered yes is {}".format(nb_question))
print("The number of questions which everyone answered yes is {}".format(yes))
#####################################################################
#                                                                   #
#   Name: AOC_Day08.py                                              #
#                                                                   #
#   Author: Titouan "Dr_LuX" Allain                                 #
#   Date created: 07/12/20 22:00                                    #
#   Last modification: 08/12/20 20:28                               #
#                                                                   #
#   Thanks to Gouderg for enlightening me about how to take this    #
#   puzzle.                                                         #
#   https://github.com/Gouderg                                      #
#                                                                   #
#####################################################################

def check(pos_to_change,instruction_list):
    used_instruction_list = list()
    pos_arg = 0
    # Execution of the instruction with modification
    while(True):
        # List the used instruction
        used_instruction_list.append(pos_arg)
        splited_arg = instruction_list[pos_arg].split(" ")
        # Jmp statement
        if splited_arg[0] == "jmp":
            # Jmp to change to a nop statement
            if pos_to_change == pos_arg:
                pos_arg += 1
            # Normal jmp statement
            else:
                pos_arg += int(splited_arg[1])
        # Nop statement
        elif splited_arg[0] == "nop":
            # Nop to change to a jmp statement
            if pos_to_change == pos_arg:
                pos_arg += int(splited_arg[1])
            # Normal nop statement
            else:
                pos_arg += 1
        # Acc statement
        else:
            pos_arg += 1
        # Infinite loop statement
        if pos_arg in used_instruction_list:
            return(False)
        # Correction execution statement
        if pos_arg == len(instruction_list):
            return(True)
        

def main():
    acc_value = 0
    instruction_list = list()
    pos_arg = 0

    with open("data8.txt","r") as f:
        lines = f.read().splitlines()
        # Copy all instruction in a list
        for line in lines:
            instruction_list.append(line)
        # Identify the corrupted instruction and count the right accumalator's value
        while(True):
            splited_arg = instruction_list[pos_arg].split(" ")
            # Acc statement
            if splited_arg[0] == "acc":
                acc_value += int(splited_arg[1])
                pos_arg += 1
            # Jmp statement
            elif splited_arg[0] == "jmp":
                # Succes execution with changing this instruction state
                if check(pos_arg,instruction_list):
                    pos_arg += 1
                # Failure execution with changing this instruction state
                else:
                    pos_arg += int(splited_arg[1])
            # Nop statement
            else:
                # No check statement. We can't check if we can change to a "JMP +0" instruction, it's an infinite loop 
                if int(splited_arg[1]) == 0:
                    pos_arg += 1
                # Check statement
                else:
                    # Succes execution with changing this instruction state
                    if check(pos_arg,instruction_list):
                        pos_arg += int(splited_arg[1])
                    # Failure execution with changing this instruction state
                    else:
                        pos_arg += 1
            # End statement
            if pos_arg == len(instruction_list):
                break
    print("After have changed the corrupted instuction, the value of the accumulator is {}".format(acc_value))

if __name__ == "__main__":
    main()
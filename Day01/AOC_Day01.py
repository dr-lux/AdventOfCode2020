#####################################################################
#                                                                   #
#   Name: AOC_Day01.py                                              #
#                                                                   #
#   Author: Titouan "Dr_LuX" Allain                                 #
#   Date created: 01/12/20                                          #
#   Last modification: 04/12/20 00:11                               #
#                                                                   #
#   Thanks to Virkin for show me some optimization about my code !  #
#   https://github.com/Virkin                                       #
#                                                                   #
#####################################################################

with open("data1.txt","r") as f:
    lines = f.readlines()
    for firstNum in lines:
        firstNum = int(firstNum)
        for secondNum in lines:
            secondNum = int(secondNum)
            for thirdNum in lines:
                thirdNum = int(thirdNum)
                if firstNum + secondNum + thirdNum == 2020:
                    print("{}".format(firstNum*secondNum*thirdNum))

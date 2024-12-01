# ***      ***
# *  *   *   *
# *    *     *
# *          *
# *          *               
for row in range(5):
    for col in range(12):
        if (col == 0 or col == 11) or (row == 0 and ((col>0 and col <3) or (col >8 and col <11)  ) or ( row == 1 and ( col == 3 or col == 7)) or ( col == 5 and row == 2 )) :
            print("*", end = "")
        else:
            print(end = " ")
    print()
    
    
# ******  
# *      *
# *       *
# *       *
# *      *
# ******
# * *
# *   *
# *     *
# *       * 
# *         *
# ***********  

for row in range(11):
    for col in range(11):
        if (col == 0) or( (row == 0 or row == 5) and (col >0 and col <6)) or ( col == 6 and ( row == 1 or row ==4)) or (col ==7 and (row == 2 or row == 3)) or (row == 6 and col == 2 )  or (row ==7 and col ==  4) or  ( row == 8 and col == 6 ) or ( row == 9 and col == 8) or ( row == 10 and col == 10 ): 
            print("*",end = "")
        else:
            print(end = " ")
    print()
                        
# *             * 
# *             *
# *             *
# *             * 
# *             *
# *             *
# *             *
#  *           *
#    * * * * * 
# ***************   
for row in range(9):
    for col in range(15):
        if (( col == 0 or col == 14) and ( row<7 )) or ( row == 7  and ( col == 1 or col ==13 )) or  ( row == 8 and ( col == 3 or col == 5 or col == 7 or col == 9 or col == 11)):
            print("*", end = "")
        else:
            print( end = " ")
    print()             
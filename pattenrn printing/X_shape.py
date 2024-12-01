# *      *
#  *    *
#   *  *
#    **
#   *  *
#  *    *
# *      *

for row in range(7):
    for col in range(8):
        if ( (row == 0 or row ==6) and (col == 0 or col == 7 )) or (( row == 1 or row ==5 ) and ( col ==1 or col == 6) ) or (row == 2 or row == 4 ) and ( col == 2 or col == 5) or (row == 3 and ( col == 3 or col ==4)):
            print("*", end = "")
        else:
            print(end = " ")
    print()
# *                *
#  *              *
#   *            *
#    *          *
#     *        * 
#      *      *
#       *    *
#        *  * 
#         **
for row in range(9):
    for col in range(18):
        if ( row == 0 and ( col == 0 or col == 17)) or ( row == 1 and ( col ==1 or col == 16 )) or ( row == 2 and ( col ==2 or col == 15  )) or ( row == 3 and ( col == 3 or col == 14)) or ( row == 4 and (col == 4 or col == 13 )) or ( row == 5 and (col == 5 or col == 12 ))or ( row == 6 and (col == 6 or col == 11 ))or ( row == 7 and (col == 7 or col == 10))or ( row == 8 and (col  == 8 or col == 9)):
            print("*", end = "")
        else:
            print(end = " ")
    print()
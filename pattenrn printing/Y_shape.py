#  *       *
#   *     *
#    *   *
#      *
#      * 
#      *
for row in range(6):
    for col in range(9):
        if ( row == 0 and ( col == 0 or col == 8)) or ( row == 1 and ( col == 1 or col == 7)) or ( row == 2 and ( col == 2 or col == 6) ) or ( col == 4 and (row == 3 or row == 4 or row == 5)):
            print( "*",end = "")
        else:
            print( end = " ")
    print()
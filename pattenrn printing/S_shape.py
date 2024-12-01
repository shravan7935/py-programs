#     *********
#   *          *
#   * 
#     *********
#              *
#    *         *
#     *********


for row in range(7):
    for col in range(12):
        if (row == 0 and (col != 1 and  col !=1) ) or ( row == 1 and ( col == 0 or col == 10)) or ( row == 2 and col ==0) or ( row == 4 and col == 10) or (row == 5 and (col == 0 or col == 10)):
            print("*", end = "")
        else:
            print(end = " ")
    print()
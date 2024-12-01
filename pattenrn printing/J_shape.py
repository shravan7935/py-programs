    # *********
    #     *
    #     *
    #     *
    # *   *    
    # *   *
    # ***** 

for row in range(7):
    for col in range(9):
        if ((col == 4) or (col == 0 and( row >3))) or ((row== 0) or (row ==6 and (col <4))):
            print("*",end = "")
        else:
            print( end = " ")
    print()
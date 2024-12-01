# ********
# *
# *   
# *   ****
# *      *
# ********
for row in range(6):
    for col in range(8):
        if ((col ==0) or (col == 7 and row >2)) or (row ==0  or row ==5 or (row ==3 and (col>3)) ):
            print("*",end ="" )
        else:
            print(end = " ")
    print()
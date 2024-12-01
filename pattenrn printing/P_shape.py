# *********
# *        *
# *        *
# *        *
# *********    
# *
# *
# *
# *
# *
   
for row in range(10):
    for col in range(10):
        if (col == 0 or (col == 9 and (row >0 and row<4))) or (( row ==0 or row == 4) and ( col != 0 and col != 9)):
            print("*", end = "")
        else:
            print(end = " ")
    print()
#    ***************
#           *
#           *
#           * 
#           * 
#           *
#           *
#           *

for row in range(8):
    for col in range(15):
        if (col == 7) or (row ==0 and ( col != 7) ):
            print( "*", end = "")
        else:
            print(end = " ")
    print()
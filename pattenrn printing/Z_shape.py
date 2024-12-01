#  * * * * * * * 
#            * 
#          *
#        * 
#      * 
#    *
#  * * * * * * * 

for row in range(7):
    for col in range(13):
        if ((row == 0 or row == 6) and ( col == 0 or col ==2 or col == 4 or col == 6 or col == 8 or col == 10 or col == 12 )) or ( row == 1 and col == 10) or ( row == 2 and col == 8)or ( row == 3 and col == 6)or ( row == 4 and col == 4)or ( row == 5 and col == 2) :
            print( "*", end = "")
        else:
            print(end = " ")
    print()

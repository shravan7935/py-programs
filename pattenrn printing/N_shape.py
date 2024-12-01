# *           *
# * *         *
# *   *       *
# *     *     *
# *       *   *
# *         * *
# *           *

for row in range(7):
    for col in range(13):
       
       if (col == 0 or col == 12) or (row == 1 and col == 2) or ( col == 4 and row == 2) or (col == 6 and row == 3) or ( row == 4 and col == 8) or (row == 5  and col == 10):
          print( "*", end = "")
       else: 
          print(end = " ")
    print()
          
        
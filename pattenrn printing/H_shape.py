# *      *
# *      *
# *      *
# ********
# *      *
# *      *
# *      *

for row in range(7):
    for col in range(8):
        if (col == 0 or col ==6) or (row == 3 and ( col>0 and col<7)):
            print("*",end = "")
        else:
            print(end = " ")
    print()
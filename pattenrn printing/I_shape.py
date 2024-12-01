#  *******
#     *
#     *
#     *
#     *
#  *******

for row in range(6):
    for col in range(7):
        if (col == 3) or (row == 0 or row == 5 and (col != 3 )):
            print("*", end = "")
        else:
            print(end = " ")
    print()
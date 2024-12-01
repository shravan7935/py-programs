# 1
# 1 2
# 1 2 3      ------> print like this 
# 1 2 3 4
# 1 2 3 4 5 

for i in range(1,6):
    for j in range(0,i):
        print(j+1,end = " ")
    print()

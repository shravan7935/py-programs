# 5 5 5 5 5
# 4 4 4 4
# 3 3 3    --------> output like this
# 2 2
# 1 


n = int(input('enter the number of column :'))
x = n+1
for i in range (1,x):
    for j in range(1,x+1-i):
        print(x-i,end = " ")
    print()
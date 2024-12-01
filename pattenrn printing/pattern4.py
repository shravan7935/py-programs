num = int(input("enter the number of row :"))
for i in range(0,num):
    for j in range(num-i-1):
        print(end = " ")
    for j in range(0,i+1):
        print("*" ,end = " ")
    print()
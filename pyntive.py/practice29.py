# count the total number of digits in a number
num = int(input("enter the number in which you want to check the number of digits :"))
count = 0
while num !=0:
    num = num // 10
    count += 1

print("total digits are :",count)


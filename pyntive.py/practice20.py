# accept a list of float numbers as an input from the user

numbers = []
for i in range(1,6):
    print("enter number ",i,':')
    item = float(input())
    numbers.append(item)

print("user list :",numbers)


number = 7536
print("Given number", number)
while number > 0:
    digit = number % 10
    number = number // 10
    print(digit,end = ' ')

 
previous_number = 0

for i in range(1,11):
    current_number = i 
    sum = previous_number+ current_number
    
    print(f"current number is {current_number} previous_number is {previous_number} and sum : {sum}")
    previous_number = i
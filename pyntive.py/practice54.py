string = "PyNaTive"

lowerList = []
upperList = []

for char in string:
    if char.islower():
        lowerList.append(char)
    else:
        upperList.append(char)
sorted_str = ''.join(lowerList + upperList)
print( sorted_str)


string = input(" enter the string that you want the middle three character :")
l = int(len(string)/2)
x = string[l]
y = string[l-1]
z = string[l+1]
newString = str( x+ y +z)
print(newString)
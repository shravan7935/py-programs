s1 = "America"
s2 = "Japan"
length1 = int(len( s1)/2)
length2 = int(len(s2)/2)
x  = s1[length1]
y = s1[0]
z = s1[-1]
a = s2[length2]
b = s2[0]
c = s2[-1]
new_string = str(y + b + x + a + z + c)
print( new_string)
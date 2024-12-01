s1 = "Abc"
s2 = "Xyz"
# mixed = s1[0] +s2[0] + s1[1]+s2[1] + s1[2] + s2[2]
# print(mixed)
s1_length = len(s1)
s2_length = len(s2)

length = s1_length if s1_length>s2_length else s2_length
result = ""
s2 = s2[::-1]

for i in range (length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)

    
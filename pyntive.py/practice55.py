
def find_digit_char_symbol(givenstr):
   char_count = 0
   digit_count = 0
   symbol_count = 0

   for char in givenstr:
     if givenstr.isalpha():
       char_count += 1

     elif givenstr.isdigit():
       digit_count += 1
     else:
       symbol_count += 1
   print("chars = ",char_count, "digits = ",digit_count, " symbol = ",symbol_count)

given_str = "P@yn2at&#i5ve"
print("total count of chars, digits and symbols \n ")
find_digit_char_symbol(given_str)
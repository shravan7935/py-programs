# inputx = int(input("enter base:  \n enter exp:"))

def exponent(base,exp):
    num = exp
    if num <0:
     print("exponent can't be negative")
    else:
     result=  base**num
    print(base,"raise to the power of ",exp,"is:",result) 

    
exponent(2,5)
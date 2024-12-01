# to get fibonacci sequence 

def fibo(n):
    a = 0 
    b = 1
    if n ==1:
        print(a)
    else:
        print(a, end = " ")
        print(b, end = " ")
        for i in range(2,n):
           c = a + b 
           a = b 
           b = c 
           print(c, end = " ")
print("fibonacci sequence :")
fibo(10)

 
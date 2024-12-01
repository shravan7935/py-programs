#recursive function 

def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0
result = addition(10)
print(result) 

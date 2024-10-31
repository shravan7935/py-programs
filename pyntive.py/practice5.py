
list1 = [ 1,2,3,4,5,6,1]
list2 = [ 20,10,30,40,50,10000000]

def  true_or_false(list):
    if list[0] == list[-1]:
        return True 
    return False
print(true_or_false(list1))
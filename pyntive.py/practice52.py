
def append_middle(s1 ,s2):
    print("original strings are ", s1, s2)
    mi =int(len(s1)/2)
    x = s1[:mi:]
    x = x+ s2
    x = x + s1[mi:]
    print("after appending new string in middle:",x)

append_middle("Ault","kelly")


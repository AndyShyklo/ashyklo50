f = open("krewes.txt", "r")
j = f.read()

t = True
while t:
    x = j.find("@@@")
    y = j[0:x]
    print(x)
    print(y)
    print(j)
    t = False
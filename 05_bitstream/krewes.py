'''
  Ankita Saha, Andy Shyklo, Abidur Rahman
  Python Pigs
  SoftDev
  K5 - Bitstream
  2024-9-18
  time spent: 0.7 hours
  '''

import random

f = open("krewes.txt", "r")
j = f.read()

t = 0
g = j.split("@@@")[:-1]

print(g)

h = []
for hx in g:
    gx = hx.split("$$$")
    print(hx.split("$$$"))
    h.append(gx)

print(h)

dictP = {4: {}, 5: {}}

for gx in h:
    print(gx[0])
    print(gx)
    if gx[0] == "4":
        dictP[4][gx[1]] = gx[2]
    elif gx[0] == "5":
        dictP[5][gx[1]] = gx[2]
    else:
        print("h")
    
print(dictP)

a = random.randint(0, len(dictP.get(4)) + len(dictP.get(5)) - 1)
print(a)
print(f"Total amount of students: {len(dictP.get(4)) + len(dictP.get(5)) - 1}")
print(f"Index: {a}")
period = 0
if (a<len(dictP.get(4))):
    b = random.choice(dictP.get(4))
    period = 4
    print(b)
else:
    b = random.choice(dictP.get(5))
    period = 5
    print(b)
print(f"Period: {period}, Name: {b}")
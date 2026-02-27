"""
pass
break
continue
"""

for a in [1, 2, 3, 4, 5, 6]:
    pass




print("Starting")
for b in [1, 2, 3, 4, 5, 6]:
    if b == 3:
        break       # exit from loop
    print(b)
print("ended", end="\n\n")




print("Starting")
for c in [1, 2, 3, 4, 5, 6]:
    if c == 3:
        continue       # return to first line of loop
    print(c)
print("ended", end="\n\n")



n = 0
while n < 20:
    n += 1
    if n % 3 == 0 and n % 5 == 0:
        print("Hiphoop")
        continue
    if n % 3 == 0:
        print("Hip")
        continue
    if n % 5 == 0:
        print("Hop")
        continue
    print(n)
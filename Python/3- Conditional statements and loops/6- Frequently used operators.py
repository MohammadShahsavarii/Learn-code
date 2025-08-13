"""
rane
enumerate
zip
in
min
max
random
input
"""

# range

for a in range(10):
    print(a)

print("###" * 20, end="\n\n")




for i in range(5):
    for j in range(4):
        print(i, j)
    print()




for i in range(6):
    for j in range(6):
        print(i*j, end="\t")
    print()



for i in range (1, 8, 2):
    print(i, end=" ")
print()



for i in range (10, 1, -2):
    print(i, end=" ")

print()

# Enumerate
l = "jadi"
for i in range(len(l)):             # can use instead of this with enumerate
    print(i, l[i])


l = ["jadi", 5, "sara"]
for i, a in enumerate (l):
    print(i, a)


# zip
name = ["sara", "bita", "sina"]
family = ["mir", "par", "zar"]
for x in zip (name, family):
    print(x)


# in
print("bita" in name)
print("per" in family)

s = "abcdef"
if 'j' in s:
    print("exist")
else:
    print("nu exist")



name = ["jadi", "ali", "sara"]
people = {
    "bita" : {"age" : 45, "height": 65},
    "sara" : {"age" : 32, "height": 71}
}
if "sara" in people:
    print("It is")


names = ["bita", "ali", "sara"]
people = {
    "bita" : {"age" : 45, "height": 65},
    "sara" : {"age" : 32, "height": 71}
}
for name in names:
    if name in people:
        print(f"I have {name} and age is {people[name]['age']}")
    else:
        print(f"I have no data for {name}")


# min , max
print(min(5,8,7,2,6,1,9,12))
print(max(8,7,2,6,9,1,3,0,12,4))




# random
from random import randint
print(randint(1,10))


# input
a = input("Enter a number: ")
print(type(a), a)


javab = randint(1,6)
i = int(input(" guss the number: "))
if (javab == i):
    print("Bravo")
else:
    print(f"Ops, not true.answer was {javab}, try again")
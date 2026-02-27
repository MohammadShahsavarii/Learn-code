'''
for used on iterables(lists, strings,...)

for VARIABLE in ITERABLE:
    statement
'''
from itertools import count

my_list = [1,2,6,8,'a']
for this_item in my_list:
    print(this_item)
    print(f"*2 = {this_item * 2}")
print("ended")

my_list2 = [1,2,3,4,5,6,7,8,9]
for a in my_list2:
    print(a)

print("*" * 20)


my_list3 = [2,4,5,7,8,9,11,12,15,16]
for a in my_list3:
    if a % 2 == 0:
        print(a)
    else:
        print(f"{a} is odd")


print("#" * 40)


# count even number
count = 0
my_list4 = [1,2,6,8,7,9,11,10,12]
for a in my_list4:
    if a % 2 == 0:
        count += 1
        print(a)        # 2,6,8,10,12               print_second
        print(count)    # 1,2,3,4,5                 prind_third
    print(a)            # 1,2,6,8,7,9,11,10,12      print_first
print(f"have {count} even number")      # have 5 even number


lists = [1,2,3,4,5]
for _ in lists:
    print(_)    # 1,2,3,4,5

for c in "jadi is fun":
    print(c)    # j a d i  i s  f u n


my_tuple = (8,9,'sara', 9.1)
for s in my_tuple:
    print(s)        # 8, 9, jadi, 3.1

my_tuple2 = (8,9,[1,2,3],'sara', 9.1)
for d in my_tuple2:
    print(d)        # 8,9,[1,2,3],'sara',9.1

people = (('sina', 40), ('mina',35),('javad',25))
for person in people:
    print(person)       # ('sina', 40), ('mina',35),('javad',25)

    name, age = person  # unpack
    print(f"{name} is {age} years old.")
'''
for name, age in people                         can use unpacking in loop
    print(f"{name} is {age} years old.")
'''

# dic
people = {
    'sina' : (45, 85),
    'mina' : (25, 65),
    'kaveh': (12, 102)
}
for person in people:
    print(person, people[person])   # 'sina' : (45, 85), 'mina' : (25, 65), 'kaveh': (12, 102)


people2 = {
    'sina' : (45, 85),
    'mina' : (25, 65),
    'kaveh': (12, 102)
}
for person in people2:
    print(person, people2[person][0])   # sina 45    mina 25    kaveh 12

people3 = {
    'sina' : (45, 85),
    'mina' : (25, 65),
    'kaveh': (12, 102)
}
for person, data in people3.items():
    print(f"{person} -> {data}")        # sina -> (45, 85)   mina -> (25, 65)    kaveh -> (12, 102)

for a in people3.keys():
    print(f"{a}")       # sina  mina  kaveh

for a in people3.values():
    print(f"{a}")           # (45, 85)    (25, 65)    (12, 102)

'''
in dictionary:
want to return key and value:

for k, v in dic.items():        k = retutn keys, v = return values
'''
for k,v in people3.items():
    print(k,v)

for i in range (1,4):
    print(i*2)


words = ["Python", "is", "awesome"]
result = ""
for word in words:
    result += word[0]
print(result)
# List Comprehension        list_variable = [x for x in iterable]

ls = [0, 0.45, 9, -1]
new_l = []                             # list comprehension
for n in ls:                           # change into this:      new_l = [x * 2 for x in ls]
    new_l.append(n * 2)
print(new_l, end="\n\n")


ls = [0, 0.45, 9, -1]
new_ls = [a * 2 for a in ls]
print(new_ls, end="\n\n")


"""
This is not in list comprehension but is funny
"""
# for check even or odd numbers:
e = 5
result = "odd" if e % 2 != 0 else "even"
print(f"5 is {result}.", end="\n\n")



# create new list just with even numbers of first list
ls2 = [0, 0.45, 9, -1, 2, 3, 6]
nw_l = [n for n in ls2 if n % 2 == 0]
print(nw_l)



l2 = [1, 2, 3, 4, 6, 5, 7, 8, 0]
nl = ["Even" if n % 2 == 0 else "Odd" for n in l2 ]
print(nl)


newl2 = ["Hop" if n % 3 == 0 else n for n in range(1, 12)]
print(newl2)
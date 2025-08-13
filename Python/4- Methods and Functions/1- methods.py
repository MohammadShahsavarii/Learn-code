'''   https://docs.python.org/3/tutorial/datastructures.html   '''

l = [1, 2, 3, 4]
print(l.pop())
print(l)

l.append(9)
print(l)

ls = [1, 2, 3, 4]
print(ls.pop(2))
print(ls)

help(l.pop)             # Provides information about '.pop' performance
#help(l.pop())           # It does two things:
"""                         1. First, l.pop() is executed.(4 is removed from the list)
                            2. Then, help() is run on the output of l.pop(), that is  4. 
                                Since 4 is not a function and there is no help for it, Python displays an error.
"""


name = "sara"
print(name)

print(name.upper())


# without ordin, each element just one time(تکراری ندارد)
# for use set, first should define : myset = set()

myset = set()
myset.add(1)
myset.add(2)
print(myset)        # {1, 2}
print(type(myset))  # class 'set'
myset.add("sara")
print(myset)        # {1, 2, "sara"}


chess = set()
chess.add("mona")
chess.add("leila")
drawing= set()
drawing.add("sara")
drawing.add("mona")
print(drawing.union(chess))         # {'leila', 'sara', 'mona'}
print(drawing.intersection(chess))  # {'mona'}


animals = set(["wolf", "dog", "cat", "tiger", "fok"])
print(animals)  # {'wolf', 'cat', 'fok', 'dog', 'tiger'}
print(type(animals))   # class 'set'
animals.add("horse")
print(animals)  # {'cat', 'fok', 'horse', 'wolf', 'tiger', 'dog'}


SetA = {1, 2, 3, 4}
SetB = {3, 4, 5, 6}
print(SetA.union(SetB))
print((SetA.intersection(SetB)))
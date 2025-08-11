# bool ( True, False)
# use in conditions ( > < >= <= ==)

age = 35
print(age == 36)     # False

# True AND True = True
# True AND False = True

# True OR False = True
# True OR True  = True

# Not True = False
# Not False = True

s = "1"
print(s.isdigit())  # True
s = "123"
print(s.isdigit())  # True
s = "1.23"
print(s.isdigit())  # False
s = "bita"
print(s.isdigit())  # False


mylist = [1, 2, 3, "mona", 3.1415]
print(2 in mylist)          # True
print( "mina" in mylist)    # False

mydic = {"dog":3, "horse":5, "cat": 2}
print("cat" in mydic)       # True
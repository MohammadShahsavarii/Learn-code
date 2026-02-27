# STRING (Șirul de caractere)           imutable

message = "Hello, my World!"         #      Hello, my W o r l d !        
#message = [from : to : step]       index:  0123456789101112131415

## Slicing (Secționare) - extragerea unei porțiuni dintr-un șir
# [from:to:step] - 'from' este inclus, 'to' este exclus
print("1)",message[0:5])  # Hello
print("2)",message[6:])   # my World!
print("3)",message[:])
print("4)",message[6:11])  # my Wo
print("5)",message[6:11:2])  # myW

print("6)",message[::2])  # Hlo ol!
print("7)",message[::-1])  # !dlroW ym ,olleH
print("8)",message[10:4:-1])  # my Wo


## methods in string (metode pentru șiruri de caractere)
name = "john"
print(name.lower())
name = name.upper() # JOHN

print(name.capitalize())  # John

number = "123456789018796537281938302461"
print(number.count("1"))  # 4
print(number.count("1", 0, 11))  # 2

favorite = "Python,cat,dog,book,movie,music"
print(favorite.split(","))  # ['Python', 'cat', 'dog', 'book', 'movie', 'music']
print(favorite.split(",", 1))  # ['Python', 'cat,dog,book,movie,music']

print(len(favorite))  # 31
print(favorite.find("cat"))  # 7
print(favorite.find("book"))  # 15
print(favorite.index("dog"))  # 11 


## String interpolation             %s -string, %i -integer, %f -float
name = "Mamal"
family_name = "shah"
age = 39.658
# old way
print("Hello" + " " + name + " " + family_name )

# old way( from C)
print("Hello %s %s, you are %i" % (name, family_name, age))
print("Hello, my name is %s and I am %d years old." % ("John", 30))

#format string
print("Hello, you are {} {}, you are {}".format(name, family_name, age))
print("Hello, you are {0} {1}, you are {2}".format(name, family_name, age))
print("Hello, you are{2} {0}, you are {1}".format(name, family_name, age))
print("Hello, you are{nam} {famil}, you are {sen}".format(nam=name, famil=family_name, sen=age))

                                #precisione {variable:num of digits.number of decimal places}
print("Hello, you are{nam} {famil}, you are {sen:1.1f}".format(nam=name, famil=family_name, sen=age))
print(f"Hello, you are {name} {family_name}, you are {age}")

#newest way
## f-string
print(f"Hello, you are {name} {family_name}, you are {age}")
print(f"Hello, you are {name} {family_name}, you are {age:.2f}")  # 2 digits after the decimal point
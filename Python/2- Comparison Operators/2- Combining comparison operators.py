"""
and   T and T --> True
      T and F --> False
      F and F --> False

or    T or T ---> True
      T or F ---> True
      F or F ---> False

not   not True --> False
      not False --> True
"""

print((3>2) and (4>3))  # True
print(4<2 and 5>3)      # False
print(3>2 or 5<1)       # True

weight = 120
print(150 > weight > 110)   # True == ((150 >weight) and (weight > 110))
print((150 >weight) and (weight > 110))     # True

# https://www.w3schools.com/python/python_operators.asp



a = int(input("enter number a: "))
b = int(input("enter number b: "))
c = int(input("enter number c: "))
if c>= b > a:
    print(True)
else:
    print(False)
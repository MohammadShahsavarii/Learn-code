def sum_of_numbers(a , b):
    res = a + b
    return res

n1 = 4
n2 = 6
print(sum_of_numbers(n1, n2))
# or
sum = sum_of_numbers(n1, n2)
print(sum)

#-------------------------------------------------
def display_time(name, n):
    """
    print name, n times
    name: string<type>
    n: integer<type>
    """
    for i in range(n):
        print(name)


display_time("bita", 3)

#-------------------------------------------------
"""
        with default value
"""
def display_time(name, n = 1):
    for i in range(n):
        print(name)


display_time("sara")

#-----------------------------------------------------
def power(n, t = 2):
    res = 1
    for i in range(t):
        res = res * n  # ==  res *= n
    return  res

print(power(2, 3))
print(power(4))

#----------------------------------------------------
def sum(n1, n2 = 5):
    return n1 + n2

print(sum(2, 8))
print(sum(1))
print(sum("jadi", "saman"))
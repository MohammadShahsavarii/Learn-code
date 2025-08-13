"""
def name_of_function(parameter):     # here we define function
    statements

name_of_function(argument)          # here we call function (return)

-----------------------------------------------------------------------

def name_of_function(parameter, parameter):
    statements
    return variabile            this is return result of function, not anymore

print(name_of_function(argument1, argument2))
or
result = name_of_function(argument1, argument2)
print(f"calculate: {result}")
"""

def hello():
    print("oh, hello world!")

hello()


#-----------------------------------------
def hello(name):
    for i in range(3):
        print(f"oh, hello {name}")

hello("sara")

#------------------------------------------
def hello(name):
    for i in range(len(name)):
        print(f"oh, hello {name}")

hello("shadi")

#-----------------------------------------
def say_hello_n_times(name, n):
    # return n time name
    for i in range(n):
        print(f"helooo {name}")

say_hello_n_times("bita", 2)
say_hello_n_times("javad", 1)

#------------------------------------------
def sum_of_numbers(a, b):
    """when we use return, its not return """
    result = a + b
    return result

print(f"result is: {sum_of_numbers(4, 5)}")
print(sum_of_numbers(2, 3))

res = sum_of_numbers(6, 7)
print(res)

#--------------------------------------------
def times_of_iterate_char(s, c):
    """
    get string and a character and
    return the number of repetition of caracter in string
    s: string
    c: character
    """
    counter = 0
    for the_character in s:
        if the_character == c:
            counter += 1
    return counter

name = "emanuel"
print(f'{name} has {times_of_iterate_char(name, "e")} e')
# or
show = times_of_iterate_char(name, 'e')
print(f"{name} has {show} e")
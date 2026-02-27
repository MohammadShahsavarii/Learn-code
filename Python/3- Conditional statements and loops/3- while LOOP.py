a = 0
print("I am started")
while a <= 5:
    print(f"a is {a}")
    a+= 1
print("I am done")
print(f"finishing with {a}", end="\n\n")



# infinite loop
'''
while True:
    print("Ininite Loop")
'''

fuel = 12
print("the fuel is low")
while fuel <= 100:
    # refueling the car
    fuel += 1
print(f"fuel is {fuel}")
print("now fuel is full", end="\n\n")


x = 1
while x < 5:
    x += 1
print(x)
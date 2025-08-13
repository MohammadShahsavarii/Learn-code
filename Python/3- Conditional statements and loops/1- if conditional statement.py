'''
if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
else:
    statement4
'''


age = 35
if age<18:
    print("teenage")
elif age<30:
    print("young")
elif age <60:
    print("adult")
else:
    print("old")



action = "goal"
score = 0
if action == "shoot":
    print("He shot the ball.")
elif action == "pass":
    print("good pass")
elif action == "goal":
    print("goooooooooal")
    score += 1
else:
    print("good match")
if score > 0:
    print(f"Bravo, we win the match! score:{score}")
else:
    print("the game is finished")

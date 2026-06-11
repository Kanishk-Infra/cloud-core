import random

actions = [
    "You woke up","You stayed sleeping"
 ]

X = actions[random.randint(0,1)]

print(X)

if X == "You woke up":
    print("You get off the bed")

elif X == "You stayed sleeping":
    print("You are sound asleep")
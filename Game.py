import random

print "Welcome to my trap. To escape you must guess the number I've randomly selected....Good luck"

answer = random.randrange(10)

guess = int(raw_input("Pick a number 0-10: "))

while guess != answer:
    if guess > answer:
        print("That's not it, you're too high")
    if guess < answer:
        print("That's not it, you're too low")
    guess = int(raw_input("Pick again: "))
else:
    print("Good Job! You're now free")
          

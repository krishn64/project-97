import random


randInt = random.randrange(1, 10)

chanceCount = 0

print("Guess a number from between 1 and 9")
print("you have 5 chances")

while chanceCount < 5:
    guess = int(input("Enter your guess: "))
    chanceCount = chanceCount + 1

    if guess < randInt:
        print("Too low! Guess a number higher than ", guess)
        
    if guess > randInt:
        print("Too high! Guess a number lower than ", guess)

    if guess == randInt:
        print("You win!!!")
        break

    if not chanceCount < 5:
        print("You lose! The number is ", randInt)
import random
play=True
number=str(random.randint(10,35))
print("I will think of a random from 10 to 35, and you have to guess it. If you guess correctly, the game will end and you will win. Make sure you guess the numeber one number and a time.")
while play:
    guess=input("Give me your guess: ")
    if number ==guess:
        print("You win the game")
        print ("The number was",number)
        break
    else:
        print("Your guess isn't right. Try again.")
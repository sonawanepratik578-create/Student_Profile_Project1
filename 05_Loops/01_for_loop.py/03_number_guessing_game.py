import random
guess = 0
attempts = 0
secret = random.randint(1,100)

while guess != secret and attempts < 5:
    guess = int(input("guess the number:"))
    attempts += 1
    
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Congrats you guess the number")
        print("Attemts:",attempts)
        
if guess != secret:
    print("Game Over!")
    print("The guess number was",secret)
        
    
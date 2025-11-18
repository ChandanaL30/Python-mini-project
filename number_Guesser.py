import random
def number_guesser():
    print("Welcome to Number Guesser!")
    level=input("Choose level(easy/hard):").lower()
    max_num=50 if level=='easy' else 100
    secret=random.randint(1,max_num)
    attempts=0
    while True:
        guess=int(input(f"Guess(1-{max_num}):"))
        attempts+=1
        if guess==secret:
            print(f"You won in {attempts} guesses!")
            break
        elif(guess<secret):
            print("Too low!")
        else:
            print("Too high!")
number_guesser()
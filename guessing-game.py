import random

print()
print("Guessing Game")
print()

while True:
    attempt = 1
    lives = 20
    roll = random.randint(1, 10000)

    while attempt <= lives:
        guess = int(input(f"Guess a number between 1 - 10000 (Attempt {attempt}/{lives}): "))
        if guess > roll:
            print("Too High")
            attempt += 1
        elif roll > guess:
            print("Too Low")
            attempt += 1
        elif guess == roll:
            print("Correct")
            break
        else:
            print("Number not recognizable")

    if guess == roll:
        print(f"It took you {attempt} attempts to get it right!")
    else:
        print(f"Sorry, you're out of attempts! The correct number was {roll}.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    print()
    if play_again != "yes":
        break

print("Thanks for playing!")
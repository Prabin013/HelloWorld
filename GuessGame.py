secret_number = 9

guess_Count = 0
max_Guess = 3

while guess_Count  < max_Guess :
    guess = int(input("Guess: "))
    guess_Count +=1
    if guess == secret_number:
        print("You have guessed the secret number!")
        break
else:
    print("Sorry u have maxed out the number of guesses allowed!!")
import random


def guessingGame(guessLimit, number):
    randomNumber = random.randint(1, number)
    try:
        while guessLimit > 0:
            guess = int(input("Enter Your Number:"))
            guessLimit -= 1
            if randomNumber == guess:
                print("Congrats.....You got Right Answer")
                break
            elif guess > number:
                print("Your Guess is out of range!")
                print(f"You have {guessLimit} guess chances left")
            else:
                print("Sorry...That was wrong!")
                print(f"You have {guessLimit} guess chances left")
        print(f"The random Number was {guessLimit}")
    except ValueError:
        print("Only Integers Allowed")


def easy():
    print("You have to guess a number between 1 and 10, and you have 6 guesses")
    guessingGame(6, 10)


def medium():
    print("You have to guess a number between 1 and 20, and you have 4 guesses")
    guessingGame(4, 20)


def hard():
    print("You have to guess a number between 1 and 50, and you have 3 guesses")
    guessingGame(3, 50)


def try_again():
    again = input("Do you want to play again? Yes/No:")
    if again.upper() == "YES":
        welcome()
    elif again.upper() == "NO":
        print("Thanks for Playing")
    else:
        print("Wrong input")
        try_again()


def welcome():
    print("Welcome to Guessing Game..!!")
    difficulty = input("Choose your level between Easy,Medium and Medium: ")
    if difficulty.upper() == "EASY":
        easy()
        try_again()
    elif difficulty.upper() == "MEDIUM":
        medium()
        try_again()
    elif difficulty.upper() == "HARD":
        hard()
        try_again()
    else:
        print("wrong input")
        welcome()


welcome()

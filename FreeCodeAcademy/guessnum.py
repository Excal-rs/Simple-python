import random

def int_check(prompt):
    while True:
        try:
            x = int(input(prompt))
            break
        except ValueError:
            print(f'Error: Input is not a integer! Please try again \n')
    return x

def str_check(prompt):
    string = str(input(prompt))
    result = all(chr.isalpha() for chr in string)
    while result == False:
        print("Error: String cannot contain non-alphabetical characters! Please try again \n")
        string = str(input(prompt))
        result = all(chr.isalpha() for chr in string)
    return string


def main(MIN, MAX):

    RANDOM_NUM = random.randint(MIN, MAX)
    print(RANDOM_NUM)

    GUESSES = 5



    lives = GUESSES 

    for i in range(GUESSES):
        print(f"You have {lives} guesses left!")
        guess = int_check("Enter your Guess: ")
        if guess == RANDOM_NUM:
            print("Well done! That is correct!")
            print(f"\nIt took you {GUESSES - lives + 1} guesses to get the right answer!")
            print(f"The answer was {RANDOM_NUM}")

            break
        elif guess > RANDOM_NUM:
            print("Too high! Try a lower number\n")
            lives -= 1
            continue
        elif guess < RANDOM_NUM:
            print("Too low! Try a higher number\n")
            lives -= 1
            continue
    else:
        print("\n\noops..you ran out of lives")
        print(f"The answer was {RANDOM_NUM}")


if __name__ == '__main__':
    MIN_NUM = 1
    MAX_NUM = 100


    print("# Welcome to Num Guesser! #")
    print("In this small game you will attempt to guess a number\n")
    print(f"The highest the number can be is {MAX_NUM}")
    print(f"The lowest the number can be is {MIN_NUM} \n")
    print(f"You have {GUESSES} guesses! \nGood Luck")

    while True:
        main(MIN_NUM, MAX_NUM)

        playerChoice = str_check("Do you want to play again: y/n").lower()

        if playerChoice in ['y', "yes"]:
            continue
        elif playerChoice in ['n', "no"]:
            print("Goodbye...")
            break
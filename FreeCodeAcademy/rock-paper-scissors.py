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



while True:
    rounds = int_check("How many rounds: (must be an odd number) ")

    if rounds % 2 == 0:
        print("Error: Must be an odd number! \n\n")
        continue
    elif rounds % 2 != 0:
        break


CHOICES = ["rock", "paper", "scissors"]

playerScore = int()
botScore = int()


for i in range(rounds):
    playerGuess = str_check("Choose: rock, paper, scissors \n")
    botGuess = random.choice(CHOICES)

    print(f"Bot chooses : {botGuess}")

    if playerScore > (rounds/2):
        print("Congrats you win! :)\n")
        break
    elif botScore > (rounds/2):
        print("Too bad... you lost :(\n")
        break
    


    elif playerGuess == botGuess:
        print("Draw! Goodluck on the next round\n")
        continue


    elif playerGuess == CHOICES[0]: #rock
        if botGuess == CHOICES[1]:
            print("You lose! Too bad, better luck next time...\n")
            botScore += 1
            continue
        
        elif botGuess == CHOICES[2]:
            print("You win!\n")
            playerScore += 1
            continue



    elif playerGuess == CHOICES[1]: #paper
        if botGuess == CHOICES[2]:
            print("You lose! Too bad, better luck next time...\n")
            botScore += 1
            continue
        
        elif botGuess == CHOICES[0]:
            print("You win!\n")
            playerScore += 1
            continue



    elif playerGuess == CHOICES[2]: #scissors
        if botGuess == CHOICES[1]:
            print("You lose! Too bad, better luck next time...\n")
            botScore += 1
            continue
        
        elif botGuess == CHOICES[2]:
            print("You win!\n")
            playerScore += 1
            continue
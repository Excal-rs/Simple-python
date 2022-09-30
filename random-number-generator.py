import random

while True:
    try:
        a = int(input("What would you like the lower bound for the random number generator to be? "))
        break
    except ValueError:
        print("Error: Please enter a valid integer! \n")
        # asks for lower bound while ensuring the program is not stopped by a invalid input e.g "hello"

while True:
    try:
        b = int(input("What would you like the upper bound for the random number generator to be? "))
        break
    except ValueError:
        print("Error: Please enter a valid integer! \n")
        # asks for upper bound while ensuring the program is not stopped by a invalid input e.g "hello"

num = random.randint(a,b)
print(num)
#output

#Github Excal-rs

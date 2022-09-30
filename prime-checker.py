import math

#user input
while True:
    try:
        num = int(input("Please enter a integer you want check for being prime: "))
        break
    except ValueError:
        print("Error: Please enter a integer! \n")
        # makes sure a integer is entered

max_num = math.ceil(math.sqrt(num))
#makes it more efficient by making it only need to try fewer numbers

if num == 1 or num == 4:
    print(f"{num} is not prime")
    #deals with how 1 and 4 did not work with this system - refer to issue #1

else:
    
    for n in range(3, max_num, 2):
    # ensures number is always odd using a count step of two
    
        if num % n == 0 or num % 2 == 0:
            print(f"{num} is not prime.")
            break      
    else:
        print(f"{num} is prime")
    #output



#Excal-Rs Github

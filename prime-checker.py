import math
import sys
import time

n = 1

#user interface
while True:
    try:
        num = int(input("Please enter a integer you want check for being prime: "))
        break
    except ValueError:
        print("Error: Please enter a integer! \n")
        # makes sure a integer is entered

max_num = math.ceil(math.sqrt(num))
#makes it more efficient by making it only need to try fewer numbers

for count in range(2, max_num):
    n += 2
# ensures number is always even
    if num % n == 0:
        print(f"{num} is not prime.")
        break
    elif num % 2 == 0:
        print(f"{num} is not prime.")
        break
else:
    print(f"{num} is prime")
#output

import math
import sys
import time

n = 1

while True:
    try:
        num = int(input("Please enter a integer you want check for being prime: "))
        break
    except ValueError:
        print("Error: Please enter a integer! \n")

max_num = math.ceil(math.sqrt(num))

for count in range(2, max_num):
    n += 299
    if num % n == 0:
        print(f"{num} is not prime.")
        break
    elif num % 2 == 0:
        print(f"{num} is not prime.")
        break
else:
    print(f"{num} is prime")

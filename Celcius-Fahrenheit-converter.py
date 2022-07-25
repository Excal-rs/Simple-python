# A program to convert Fahrenheit to Celsius and vise-vera

import sys
import time

# Converts Fahrenheit to Celsius
def F2C(F):
    Celsius = 5 / 9 * (F - 32)
    return Celsius


# Converts Celsius to Fahrenheit
def C2F(C):
    Fahrenheit = (C * 1.8) + 32
    return Fahrenheit

# Prompt for user input
X2Y = input("Would you like to Convert Fahrenheit or Celsius? ")

while X2Y.lower() not in ['c', "celsius", 'f', "fahrenheit"]:
    print("Error! Please enter an appropriate input. \n", file=sys.stderr)
    time.sleep(0.1)
      #Ensures the error comes before the prompt
    X2Y = input("Would you like to Convert Fahrenheit or Celsius? ")

X = float(input(f"What is the temperature in {X2Y} ?"))

if X2Y.lower() in ["celsius", 'c']:
    print(f"{X} degrees Celsius is {C2F(X)} degrees fahrenheit")
elif X2Y.lower() in ["fahrenheit", 'f']:
    print(f"{X} degrees Fahrenheit is {F2C(X)} degrees Celsius ")

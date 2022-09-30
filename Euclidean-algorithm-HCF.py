# A program that utilises the Euclidean algorithm to find HCF
while True:
    try:
        a = int(input("Enter a number: "))
        break
    except ValueError:
        print("Error: Please enter a valid integer! \n")

while True:
    try:
        b = int(input("Enter another number: "))
        break
    except ValueError:
        print("Error: Please enter a valid integer! \n")



def computeGCD(x, y):
    while (y):
        x, y = y, x % y
        # swaps x and y variable while making y, x mod y
    return abs(x)



print(f"The HCF of {a} and {b} is : {computeGCD(a,b)}")
#output

#Excal-rs Github

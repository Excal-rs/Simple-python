# This is a simple program for finding the sum of digits in python 

def getAns(n):
    sum = 0
    while (n != 0):
        sum += int(n % 10)
        #Gets the digit
        n = n // 10
        # You can also do "n = int(n/10)"
    return sum

# Call Function
num = int(input("Enter a poitive integer:".rstrip()))
print(f"The sum of the digits of the number {num} is: {getAns(num)}")

#Excal-rs Github

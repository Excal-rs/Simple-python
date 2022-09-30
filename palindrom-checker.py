string = str(input("Please enter a phrase or word to check if it is a palindrome: \n"))

def rmSpaces(s):
    s = s.replace(' ', '')
    return s
# removes spaces for phrases e.g race car

string2 = rmSpaces(string)

if string2[::-1].lower() == string2.lower():
    print(f"Guess what! {string},  is a palindrome! :)")
else:
    print(f"{string}, is not a palindrome. :(")
    #output

#Excal-rs Github

# So as of starting these projects I do not know what a "madlib" is but I have heard of it
# After some research I believe it is a story with modular verbs, people, nouns, adjectives etc

# Skills: Concatenation, User input, User input validation, List comprehension

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




num1 = int_check("Please enter a number: ")
num2 = int_check("Please enter another number: ")

celebname = str_check("Please enter a celebrities first name: ")
name1 = str_check("Please enter name of the first character: ")
name2 = str_check("Please enter name of the second character: ")

event = str_check("Please enter a event that involves the two characters: ")



RELATIONSHIP_OPTIONS = ["Friends", "Siblings", "Lovers", "Colleague", "Other"]
relationship = str(input(f"\nPlease enter the relationship between the two characters from the following options:\n{RELATIONSHIP_OPTIONS}\n"))
COMPARABLE_OPTIONS = [element.lower() for element in RELATIONSHIP_OPTIONS]

while relationship.lower() not in COMPARABLE_OPTIONS:
    print("Error: That is not a correct option! Please try again")
    relationship = str(input(f"\nPlease enter the relationship between the two characters from the following options:\n{RELATIONSHIP_OPTIONS}\n"))



animal = str_check("Please enter a species of animal: ")

noun = str_check("Please enter a noun: ")
verb = str_check("Please enter a verb (ending in -ing): ")
verb2 = str_check("A verb that a animal would do (ending in -ed): ")

meansOfTransport = str_check("Please enter a means of transport: ")
emotion = str_check("A human emotional feeling: ")



story = f"""\n\nWhile {name1} was {verb} for {num1} {noun} to be used at the upcoming {event}, 
{name2} was getting {verb2} by {celebname}'s {animal}! But then {name2} saw {num2} {noun} and felt {emotion}
Back again with {name1} as they were {verb} they heard {name2}, they used {meansOfTransport} to get their but got distracted as they saw {celebname} and their {animal},
completely oblivious to {name2}
"""

print(story)
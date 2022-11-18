from datetime import date
from collections import namedtuple

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

DOB = namedtuple('DOB', ['day', 'month', 'year'])

DOB_str = input("Please enter Date of Birth in format \"dd mm yyyy\": ")
dob = DOB(*([int(x) for x in DOB_str.split()]))

gametime = age(dob)

print(f"You are {gametime} years old!")

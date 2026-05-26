""" so 1st i have write my code in test.py file and then i have asked chatgpt to suggest three improvements
# so it gives me 3 improvements as
# 1st improvement :- Add Input validation, For example if user doesn't write birth year in integer then it will give
us input error so we have write try block for solving this problem.
# 2nd improvement :- check for unrealistic year, if user enters birth year greater than current year or less than 1900 then 
you have to print message like please enter realistic birth year.
# 3rd improvement :- add tile so that if user enters name in small letter then it's first letter should be in capital.
"""
from datetime import datetime
current_year = datetime.now().year
name = input("Enter your name: ").title()
try:
    birth_year = int(input("Enter your birth year:"))
    if birth_year > current_year or birth_year < 1900:
        print("Please enter a realstic birth year")
    else:
        age = current_year - birth_year
    print(f"\nHello, {name}!")
    print(f"You are {age} years old in {current_year}.")
    print("Have a great day!")

except ValueError:
    print("Invalid input!, please enter numbers only")


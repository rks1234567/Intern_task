from datetime import datetime
current_year = datetime.now().year
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year:"))
age = current_year - birth_year
print(f"\nHello, {name}!")
print(f"You are {age} years old in {current_year}.")
print("Have a great day!")
""" This i have asked from claude.ai to suggest me three improvements
so it gives me like 1st improvement is Add Input validation that is also 
suggested by chatgpt
2nd improvement that is suggested by claude is wrap logic in a funtion so that
the code become reusable
3rd improvement it shows me that calculate age more accurately using birthday
"""

from datetime import date

def get_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if(today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def main():
    name = input("Enter your name:").strip()
    if not name:
        print("Name cannot be empty.")
        return
    

    try:
        birth_input = input("Enter your birth date(YYYY-MM-DD): ")
        birth_date = date.fromisoformat(birth_input)
    except ValueError:
        print("Invalid date. Please use format YYYY-MM-DD")
        return
    
    # print greeting
    age = get_age(birth_date)
    print(f"\nHello, {name}!")
    print(f"You are {age} years old. ")
    print("Have a great day!")

if __name__ == "__main__":
    main()
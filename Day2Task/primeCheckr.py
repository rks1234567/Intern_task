def primeChecker(number):
    if(number<=1):
        return False
    for i in range(2,number):
        if(number%i==0):
            return False
    return True
"""
def main():
    number = int(input("Enter a number: "))
    ans = primeChecker(number)
    print("Number is prime: ", ans)


main()
"""

# or i can do like this, i don't have to create this main function
number = int(input("Enter a number: "))
print("The number is prime: ", primeChecker(number))

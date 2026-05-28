try:
    x = int(input("Enter x:"))
    ans = (10/x)
except ZeroDivisionError:
    print("Divide by zero is not allowed")
except ValueError:
    print("Invalid Input")
else:
    print(f"ans is: {ans}")
finally:
    print("This block is always executed")
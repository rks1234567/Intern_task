def fact(number):
    result = 1
    while(number>=1):
        result = result * number
        number-=1
    
    return result


number = int(input("Enter a number:"))
ans = fact(number)
print(ans)
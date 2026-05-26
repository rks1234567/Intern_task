""" if-elif-else conditions """
grade = input("Enter your grade: ")
if(grade == 'A'):
    print("Very good Grade! Keep it up")
elif(grade == 'B'):
    print("Good!, you can do improvement in your marks ")
elif(grade == 'C'):
    print("Not as good, you have to work on yourself ")
else:
    print("Very poor grade, you have to a lot of work on yourself ")


# This is traffic light example to understand about if,elif,else conditions.
color = input("Enter color")
if(color == "red"):
    print("You have to stop!")
elif(color == "yellow"):
    print("Look")
elif(color == "green"):
    print("you can go")
else:
    print("Invalid input")

class Student:
    college_name = "ABC"   # so this is instance attribute.
    PI = 3.1

    def __init__(self, name, cgpa):  # these are instance attributes.
        self.name = name
        self.cgpa = cgpa
        self.PI = 3.14

stu1 = Student("Rohit", 9.8)
print(stu1.name)
print(stu1.college_name)
print(Student.college_name)
print(stu1.PI)


# if i print instance attribute we have to use object name. 
# but if we want to print class attribute then we can call it both using object name or class name.
        
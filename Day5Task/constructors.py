class Student:
    def __init__(self):  # this is called default constructor.
        print("Constructor are called")
        
# so how many times we call create an object it's constructor are always called.
stu1 = Student()
stu2 = Student()
stu3 = Student()

# we can also pass values to the constructor.

class Student1:
    def __init__(self, name, cgpa): # so these are called instance attributes. or this is also called parameterized constructor.
        self.name = name
        self.cgpa = cgpa
    
    def get_cgpa(self): # this is called instance methods
        return self.cgpa

s1 = Student1("Rohit",8.2)
s2 = Student1("Niharika",9.2)
s3 = Student1("Vaishnavi",9.5)

print(s1.name, s1.cgpa)
print(s2.name, s2.cgpa)
print(s3.name, s3.cgpa)

        
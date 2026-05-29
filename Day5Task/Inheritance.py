# Inheritance:- Child class can extends its parent class properties.
class Employee:
    start_time = "9AM"
    end_time = "7PM"
    def change_end_time(self,new_end_time):
        self.end_time = new_end_time

    def change_start_time(self, new_start_time):
        self.start_time = new_start_time

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role


ad1 =AdminStaff("Manager")
ad1.change_start_time("10AM")
ad1.change_end_time("8PM")
print(ad1.role, ad1.start_time, ad1.end_time)
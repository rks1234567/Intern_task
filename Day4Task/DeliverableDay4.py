# reads from the csv file
import csv

total_marks = 0
total_students = 0
with open(r"C:\Users\srs\Desktop\Git Demo\Intern_task\Day4Task\students.csv", "r") as f:
    """
    reader = csv.reader(f)
    for row in reader:
        print(row)
        """

# computes averages
    reader1 = csv.DictReader(f)
    for row1 in reader1:
        try:
            marks = int(row1["Marks"])
            total_marks += marks
            total_students +=1
        except ZeroDivisionError:
            print("Invalid input")
            break
avg = total_marks/total_students
print(f"Average marks of students is: {avg}")


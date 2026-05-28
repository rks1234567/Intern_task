import csv
highest = 0
topper = ""

with open(r"C:\Users\srs\Desktop\Git Demo\Intern_task\Day4Task\students.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        marks = int(row["Marks"])

        if(marks>highest):
            highest = marks
            topper = row["Name"]

        
print(f"Topper Student name is: {topper}")
print(f"Highest marks of topper is: {highest}")
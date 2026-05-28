import csv
# write results.csv

with open(r"C:\Users\srs\Desktop\Git Demo\Intern_task\Day4Task\students.csv", "r") as infile,\
    open(r"C:\Users\srs\Desktop\Git Demo\Intern_task\Day4Task\result.csv", "w", newline="") as outfile:
        reader = csv.DictReader(infile)
        fields = ["Name", "Age","Marks","Result"]
        writer = csv.DictWriter(outfile,fieldnames=fields)
        writer.writeheader()
        for row in reader:
                marks = int(row["Marks"])
                #result = "Pass" if marks > 40 else "Fail"
                if(marks>40):
                    result = "Pass"
                else:
                    result = "Fail"
                
                writer.writerow({
                      "Name" : row["Name"],
                      "Age" : row["Age"],
                      "Marks" : marks,
                      "Result" : result

                })
print(f"result.csv created successfully!")
                

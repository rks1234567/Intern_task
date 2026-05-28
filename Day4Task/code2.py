import json
data = {
    "name": "Rahul",
    "isStudent" : True,
    "age" : None
}

with open(r"C:\Users\srs\Desktop\Git Demo\Intern_task\Day4Task\data1.json", "w") as f:
    json.dump(data, f)
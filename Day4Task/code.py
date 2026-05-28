import json
# json_str = '{"name": "Rohit", "isStudent" : true}' 

"""
py_obj = json.loads(json_str)
print(type(json_str), json_str)
print(type(py_obj), py_obj)
"""
# if we want to convert JSON String to python object than we can use json.loads function
# if we want python object to json string then we can use json.loads.
"""
py_obj = {
    "name" : "Rohit",
    "city" : "Solan",
    "isStudent" : None
}

json_str = json.dumps(py_obj)
print(type(json_str),json_str)
"""

# Dealing with files
# for reading,we can use json.load funcion
# and for writing, we can use json.dumps function


with open(r"C:\Users\srs\Desktop\Git Demo\Intern_task\Day4Task\data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)


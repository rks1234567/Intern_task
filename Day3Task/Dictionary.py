"""Dictionary stores values in the form of key-value pairs, keys are unique
and dictionary is mutable and unordered.
"""
info = {
    "name" : "Rohit Kumar Sharma",
    "cgpa" : 8.62,
    "Subjects" : ["Java", "Pyhton","C++"]
}
print(info)

print(type(info))

info["cgpa"] = 9.8
print(info)


# Dictionary methods
print(info.keys()) # return all keys 
print(info.values()) # returns all values
print(info.items()) # return (key,value) pairs
print(info.get("name"))  # return value according to key
info.update({
    "City" : "Solan"
})
print(info)


# iteration in dict
d1 = {
    "Name" : "Rohit",
    "Age" : 23,
    "Roll_no." : 45
}

# for loop for iteration
for i in d1:
    print(d1.get(i))
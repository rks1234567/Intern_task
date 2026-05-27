# List is mutable 
marks = [70,89,65,78,95,98,69]
marks[2] = 67
print(marks[6])
print(marks)
print(len(marks))


# slicing in Lists
print(marks[2:len(marks)])
print(marks[-5:])

# list methods
marks.append(87)
print(marks)
marks.insert(1,55)
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)


"""
integers="12345678"
lst=[]
for i in integers:
    lst=[int(i)]+lst

print(lst)
"""

# for loops in a list
# Linear Search
list = [2,3,5,10,6]
idx = 0
x = 10
for i in list:
    if(i==x):
        print(f"{x} found at index {idx}")
        break
    idx+=1
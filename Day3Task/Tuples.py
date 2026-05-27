"""Tuples can functions similar to lists but they are immuatable in nature means we can not do 
assignment in this. """

tup = (1,2,3,4,5)
print(tup)
print(type(tup))

"""
# but if i want like 
tup[2] = 5
print(tup)  # so it will give us error tuple object does not support item assignment.
"""

t = (1)
print(type(t)) # so it will not be a tuple, its tpye is printed as int but if i put comma after 1 then it's type will become tuple.

t1 = (1,)
print(type(t1))  # now its type will be tuple.


# for loop in tuple
tp = (1,2,3,4,5)
sum = 0
for i in tp:
    sum +=i

print(f"Sum of tuples values is: {sum}")

# tuples methods 
tp1 = (1,2,4,2,8)
print(tp1.index(2)) # returns 1st occurance index
print(tp1.count(2)) # returns total occurances


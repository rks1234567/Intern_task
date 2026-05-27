"""Sets are collection of unique elements.
Sets can be mutable byut elements are always immutable.
Sets are mutable ans unordered.
"""

s = {1,2,3,4,2,3,2}
print(s)
print(type(s))
print(len(s))

# because sets are mutable we can add elements to it.
s.add(5)
print(s)

# for creating empty set
"""
empty_set = {} # in this way, i cannot create empty set, it is a type of dictionary
print(type(empty_set)) # it's type is <class 'dict'>
"""

# so we can create empty set as 
empty_set = set()
print(type(empty_set))  #in this way i can create an empty_set


# Set methods
s1 = {1,2,3}
s2 = {5,6}
s1.add(4) # adds a value 
s1.remove(2) # removes a value
# s1.clear() # clears the set
s1.pop() # removes a random value
s1.union(s2) # return new union

print(s1)

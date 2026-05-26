word1 = "Rohit"
word2 = "Sharma"

# for concatenation
# we can do this using two ways
print(word1 + word2)
# second way is like you can store the concatenating string in any variable and print that
sentence = (word1 + " " + word2)
print(sentence)

# In strings you can print your string using for loop
for ch in word1:
    print(ch)


# Because string is immutable in nature we cannot change its value 
# for example if i am writing like this 
# word1[2] = 'a'# it is not possible in python
print(word1[2])
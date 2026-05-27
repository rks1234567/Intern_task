sentence = input("Enter a String: ")
words = sentence.split(" ")
freq = {}
for word in words:
    if word in freq:
        freq[word] +=1
    else:
        freq[word] = 1

freq_list = list(freq.items())
freq_list.sort(key=lambda x:x[1], reverse=True)

print("Top 5 repeating words")

for i in range(5):
    if(i<len(freq_list)):
        print(freq_list[i])



# word search code for knowing concepts of how we can iterate in our text file.
data = True
word = "Python"
with open(r"C:\Users\srs\Desktop\Git Demo\Intern_task\Day4Task\sample2.txt", "r")as f:
    line = 1
    while data:
        data = f.readline()
        if(word in data):
            print(f"{word} found at line number: {line}")
            break
        line+=1

    

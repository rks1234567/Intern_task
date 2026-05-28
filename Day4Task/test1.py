# with open("Day4Task/sample.txt", "r") as f:

    # data = f.read()  # it reads all the text present inside the text file.
    # data = f.readline() # it reads line by line
    # print(data)


# Also if we want to overwrite changes in our text file then we can use
with open(r"C:\Users\srs\Desktop\Git Demo\Intern_task\Day4Task\sample.txt", "w") as f:
    f.write("Hello,this write method overwrites the text in sample.text file")

f.close()



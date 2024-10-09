with open("Demo.txt", "r") as file:
    content = file.readlines()
    print(content)
    print("No. of lines in the file are : " , len(content))

#readlines() reads all lines in a file and returns them as a list of string
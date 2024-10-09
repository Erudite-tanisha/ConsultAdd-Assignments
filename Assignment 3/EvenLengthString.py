with open("doc.txt", "r") as file1 :
    content = file1.read()
    print(content)

def Helper(data):
    data =list(content.split(" "))
    res = []
    for i in data:
        n = len(i)
        if n%2 == 0:
            res.append(i)
    output = (str)(res)
    print(output)

Helper(content)
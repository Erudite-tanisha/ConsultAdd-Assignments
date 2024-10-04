list = []
dict = {}
n = int(input("enter length of input"))
for i in range(0,n):
    element = int(input())
    list.append(element)
for i in list:
    if(i in dict):
        dict[i] += 1
    else:
        dict[i] = 1
print(dict) 


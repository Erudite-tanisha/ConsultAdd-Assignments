n = int(input("enter length : "))
list = []

for i in range(n):
    element = int(input())
    list.append(element)
    
def AddOne(list,n):
    for i in range(n+1):
        list[i] += 1
    print(list)

try:    
    AddOne(list,n)
except IndexError:
    print("index out of range")
finally:
    print("try again")
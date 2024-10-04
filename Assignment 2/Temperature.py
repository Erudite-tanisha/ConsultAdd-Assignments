n = int(input("enter length"))
l = []
for i in range(0,n):
    print("enter temperature")
    element = int(input())
    l.append(element)

def highest(l,n):
    max = l[0]
    for i in range(1,n):
        if l[i]>max:
            max = l[i]
    return max

def Lowest(l,n):
    min = 0
    l.sort()
    min = l[0]
    return min

def Average(l,n):
    sum = 0
    for i in range(n):
        sum += l[i]
    avg = sum/n
    return avg

print("Average : ",Average(l,n))
print("Highest Temperature : " ,highest(l,n))
print("Lowest : ",Lowest(l,n))
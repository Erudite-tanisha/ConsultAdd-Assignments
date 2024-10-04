n = int(input("enter length"))
l1 = []
l2 = []
for i in range(0,n):
    element = int(input())
    l1.append(element)
for j in range(0,n):
    element = int(input())
    l2.append(element)
def Common(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    s3 = s1.intersection(s2)
    return list(s3)

print(Common(l1,l2))
# print(l1)


l = [7,2,5,1,9,3]
def Median(l):
    l1 = sorted(l)
    n = len(l1)
    if n%2 == 1:
        med = l1[n//2]
    else:
        mid1 = l1[n//2-1]
        mid2 = l1[n//2]
        med = (mid1+mid2)/2

    return med
print(Median(l))
    


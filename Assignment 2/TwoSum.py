l = [0,2,3,4,5]
k = 6
def TwoSum(l, k):
    res = []
    for i in range(0,len(l)-1):
        for j in range(i+1, len(l)):
            if l[i]+l[j]==k :
                res.append(i)
                res.append(j)
    return res

print(TwoSum(l,k))


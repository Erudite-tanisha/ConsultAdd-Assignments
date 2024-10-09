n = int(input("enter no. of stones : "))
def Helper(n):
    piles = []
    if n%2 == 0:
        x = 2
    else:
        x = 1
    stones = x  
    while(stones<n):
        piles.append(stones)
        stones += 2
    return piles
print(Helper(n))

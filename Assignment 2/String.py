s = str(input("enter string : "))
k = "H"
def Helper(s,k):
    if s.startswith(k):
        return True
    else:
        return False
print(Helper(s,k))
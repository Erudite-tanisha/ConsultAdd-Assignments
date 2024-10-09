n = int(input("enter no."))
def Power(n):
    n = n/2
    if n == 2:
        return True
    elif n > 2:
        Power(n)
    else:
        return False


if Power(n):
    print ("yes")
else:
    print ("no")
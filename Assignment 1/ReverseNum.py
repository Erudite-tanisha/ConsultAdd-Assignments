num = int(input("enter num"))
rev = 0
while(num>0):
    dig = num%10
    rev = rev*10+dig
    num //= 10
print(rev)
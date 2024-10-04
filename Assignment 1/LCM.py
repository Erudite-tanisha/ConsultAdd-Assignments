num1 = int(input("enter first no. "))
num2 = int(input("enter sec no. "))
if(num1>num2):
    max = num1
else:
    max = num2
while(1):
    if(max%num1==0) and (max%num2==0):
        lcm = max
        break
    max += 1
print("LCM is : ", lcm)

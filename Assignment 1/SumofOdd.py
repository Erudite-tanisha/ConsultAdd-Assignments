sum = 0
num1 = int(input("enter first value"))
num2 = int(input("enter sec value"))
for i in range(num1, num2):
    if(i%2 != 0):
        sum += i
print(sum)
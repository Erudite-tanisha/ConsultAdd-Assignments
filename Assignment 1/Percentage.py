phy = int(input("enter phy marks"))
bio = int(input("enter bio marks"))
chem = int(input("enter chem marks"))
math = int(input("enter math marks"))
cs = int(input("enter cs marks"))

total = phy+bio+chem+math+cs
per = total/500*100
print(per)
if(per>=90):
    print("A")
elif(per<90 and per>=80):
    print("B")
elif(per<80 and per>=70):
    print("C")
elif(per<70 and per>=60):
    print("D")
elif(per<60 and per>=40):
    print("E")
else:
    print("F")
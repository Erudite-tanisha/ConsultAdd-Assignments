num=0
alphabet=0
x = str(input("enter input"))
for i in x:
    if '0' <= i <= '9':
        num += 1
    elif ('a' <= i <= 'z') or ('A' <= i <= 'Z'): 
       alphabet += 1
print(num, alphabet)
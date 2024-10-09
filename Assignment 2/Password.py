password = "hello"
def UserName():
    user = str(input("ENTER USERNAME : "))
    print(user)

def EnterPass():
    passw = str(input("ENTER PASSWORD : "))
    return passw


UserName()
EnterPass()

passw = EnterPass()
if passw!=password:
    for i in range(2):
        print("Wrong password! Try Again")
        if passw != password:
            EnterPass()
        else:
            print("WELCOME")
if passw != password:
    print("EXIT")        



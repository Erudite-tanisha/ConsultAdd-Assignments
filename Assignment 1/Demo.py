#list --> Difference between append and extend
# labhesh = "Consultadd"
# names = ["abc", "pqr", "mno", 123, None, True, labhesh]
# print(names)
# print(type(names))


# names.append("Pune")  
# print(names)

# names.pop(1)
# print(names)

# names.remove(labhesh)
# print(names)

# l1 = ["abc", "pqr", "mno", [23,11,45,["apple", "orange"]]]

#indexing --> 0 to n-1 ( n length of the list) --> (-1 to -n ) ( for negative indexing)

# print(l1[3][3][1])
# print(l1[-1][-1][-1])

# slicing --> taking a sub part of list / subarry of list / sublist of list --> 0 to n+1 

# l1 = ['a','b', 'c', 'd'] 

# d1 = {
#     "name":"John",
#     "age":56,
#     "car": ["Ford", "Toyota", "Audi"],
#     "name":"Smith"
#     }
# print(d1)


# a = 10 
# b = 10 
# print(id(a), id(b))
    

# Functions -- Functional Programming 

# function defn and function calling 

# function def --> Defing, writing down the statements you need 
# function call --> No limits to call the function, 

# def function_name(arguments......):
    # statments 
    # return 

#result = function_name(parameter)



#1st type --> No Argument No Return type 

# def function_1():
#     a = 10 
#     b = 20 
#     c = a+b 
#     print(c)

# function_1()

# 2nd Type --> Argument with No Return Type 

# def function_2(a,b):
#     c = (a+b)**2 
#     print(c)

# function_2(2,3)

# 3rd Type --> Argument with Return Type 

# def function_3(a,b):
#     c = (a+b) * (a-b) 
#     print("This is the 3rd type")
#     return c 
# print(function_3(2,3))


#4th Type --> No Arguement with Return 

# def function_4():
#     a = 25 
#     b = 30 
#     a,b = b,a 
#     print(a,b)
#     return a,b

# result = function_4()
# print(result)


# Types of Arguments 

# Postional Arguments --> Position of the arguments are important

# def concat_name(fn, ln): 
#     fn = fn + " " + ln 
#     return fn 

# print(concat_name("Jones", "Alex"))

# Keyword Arguments 

# def concat_name(fn, ln): 
#     fn = fn + " " + ln 
#     return fn 

# print(concat_name(ln="lalka", fn="Labhesh"))

# Default Argument
'''def concat_name(fn, ln, company = "Consultadd"): 
    fn = fn + " " + ln + " Working for " + company
    return fn 

print(concat_name(ln="lalka", fn="Labhesh", company = "Cloudtech"))
'''
#variable length arguments 
'''def Outer(func):
    def Inner(*args, **kwargs):
        print("before execution")
        catch = func(*args, **kwargs)
        print("after execution")
        return catch
    return Inner

@Outer
def sum(a,b):
    print("inside the function")
    return a+b'''



'''class Car :
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    def FullName(self):
        return f"{self.__brand} {self.model}"
    def get_brand(self):
        return self.__brand + "!"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

#e = ElectricCar("tesla", "Model S", "85kw")
#print(e.model)

c = Car("toyota", "corolla")
print(c.get_brand())

file = open("file.txt", "r")
read = file.read()
print(read)
print(file.tell())
'''
class Addition :
    def __init__(self):
        print("adding")
    def sum(self,a,b):
        self.a = a
        self.b = b
        print("under process")
        return a+b      

class Subtraction :
    def __init__(self):
        print("subtracting")
    def sum(self,a,b):
        self.a = a
        self.b = b
        print("under process")
        return a-b        

add = Addition()
sub = Subtraction()

for i in (add,sub):
    print(i.sum(2,4))
    print(i.sum(4,2))



























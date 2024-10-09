'''list = [1,2,3,4,5]
it = iter(list)
print(next(it))
print(type(it))
print(type(next))'''


def Generator():
    count = 0
    while(count<10):
        yield count
        count += 1
    
for i in Generator():
    print(i)
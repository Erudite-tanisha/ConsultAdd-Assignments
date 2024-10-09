list1 = ['Red', 'Blue', 'Black', 'White', 'Pink']
def Helper(s):
    return list(s)
res = list(map(Helper, list1))
print(res)
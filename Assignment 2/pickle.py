'''
import pickle
class example :
    a_number = 35
    a_string = "hey"
    a_list = [1, 2, 3]
    a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
    a_tuple = (22, 23)

e = example()
ipickle = pickle.dump(e) #pickling the object
print(f"pickled object : \n {ipickle}\n")
'''

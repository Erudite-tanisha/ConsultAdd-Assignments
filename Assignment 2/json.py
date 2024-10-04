# Python to JSON
import json
dictionary = {
"id": "04",
"name": "sunil",
"department": "HR"
}
# Serializing json 
json_object = json.dumps(dictionary, indent = 4) # there are 4 whitespaces efore each data
print(json_object)

# JSON to Python objects
import json
employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'
employee_dict = json.loads(employee)
print(employee_dict)
print(employee_dict['name'])


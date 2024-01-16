import json

def func():
    data={
        "name":"kartik",
        "std":"bca",
        "stream":10
        
        
    }
    # return data
    
    return json.dumps(data)

def func2():
    data=func()
    print(data)
    print(type(data))
    
    newdata=json.loads(data)
    print(newdata)
    print(type(newdata))
    
func2()

import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Convert JSON string to Python object
python_object = json.loads(json_string)

print(python_object)


import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert Python object to JSON string
json_string = json.dumps(data)

print(json_string)
# this is simple that in json.loads is used to for recieve data in json string 
# and json.load is used to recieve data in str json to send data in file 

# this is simple that in json.dumps is used for sending data in json str 
# this is simple that in json.dump is used for sending data in json str to file only 


#JSON: a lightweight data format used for data exchange
 #now we have a Python dict and we wanna convert/dump it to a JSON object
import json

person = {"firstName": "John", "lastName": "Smith", "age": 43, "hobbies": ["jogging", "biking", "reading"], "hasChildren": True,
          "children": [{"firstName": "Josh", "age": 7}, {"firstName": "Joey", "age": 5}]}
'''
personJSON = json.dumps(person)      #'dumps()'  will dump our Python 'dict' object to a JSON string.
print(personJSON)
#results (now it's in JSON format):  {"firstName": "John", "lastName": "Smith", "age": 43, "hobbies": ["jogging", "biking", "reading"], "hasChildren": true, "children": [{"firstName": "Josh", "age": 7}, {"firstName": "Joey", "age": 5}]}
'''
#personJSON = json.dumps(person, indent=4, separators=('; ', ' = '), sort_keys=True)
personJSON = json.dumps(person, indent=4, sort_keys=True)
#print(personJSON)
'''results (now it's in a nicer, different JSON format): 
but we don't recommended to use 'separators' as the default format is good enough. 
{
    "age" = 43; 
    "children"= [
        {
            "age" = 7; 
            "firstName" = "Josh"
        }; 
        {
            "age" = 5; 
            "firstName" = "Joey"
        }
    ]; 
    "firstName" = "John"; 
    "hasChildren" = true; 
    "hobbies" = [
        "jogging"; 
        "biking"; 
        "reading"
    ]; 
    "lastName" = "Smith"
}
'''


'''
# we can also convert/dump the Python dict into a JSON file.
 #first, we create a file in the 'write' mode as 'file', and then we use 'dump()' 
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)
#results:  a 'person.json' file is created in the current folder
'''


# Deserialization / Decoding: convert the JSON data back to a Python object
 #e.g., now we wanna convert the JSON string back to the Python dict.   'loads()'  means loading from a string
'''
person = json.loads(personJSON)
print(person)
#results:  {'age': 43, 'children': [{'age': 7, 'firstName': 'Josh'}, {'age': 5, 'firstName': 'Joey'}], 'firstName': 'John', 'hasChildren': True, 'hobbies': ['jogging', 'biking', 'reading'], 'lastName': 'Smith'}
 #it sorted (followed 'sort_keys=True').  
'''
 #e.g., convert the JSON file, we use 'load()'
  #we open it in the 'read' mode as 'file'
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)
#results:  {'firstName': 'John', 'lastName': 'Smith', 'age': 43, 'hobbies': ['jogging', 'biking', 'reading'], 'hasChildren': True, 'children': [{'firstName': 'Josh', 'age': 7}, {'firstName': 'Joey', 'age': 5}]}
 #it didn't sort









a= {"Name":"Nitesh", 
    "Address": "Kathmandu",
    "Age": 21}

print(a["Name"])
print(a.get("Age"))

a["Phone_no"]="1356135613"  #changing the content of dictionary.

print(a.get("Phone_no"))
print(a)

print(a.get("Address"))

a['Name']="Samrajya"
print(a)


del a["Age"]  #deleting any specific items from the dictionary.
print(a)

print(len(a))  #length of key value pair in dictionary.
4
print(a.keys())
print(a.values())
print(a.items())

#looping through dictionary.
for key in a:
    print(key)
    
for x in a.values():
    print(x)
    
for x in a.items():
    print(x)      
    
for key,value in a.items():
    print(key,value)
    
dicts= {"section": "Data Science", 
       "Prof": "Basha",
       "Sem": "7"}
for key, values in dicts.items():
    print(key, values)
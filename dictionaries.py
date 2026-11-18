d={"name": "narein", "age": 13}
print(d)
print(d.keys())
print(d.values())
#updating a value in the dictionary
d["age"]=14
print(d)
#adding a new element to a dictionary
d["place"]="Bahrain"
print(d)
d["month"]="November"
print(d)
#removing an item from a dictionary
del d["age"]
print(d)
#checking if key exists in dictionary
if "name" in d:
    print("Yes, this is present.")
else:
     print("No, this is not in the dictionary.")
#iterating over keys
for key in d.keys():
     print(d[key])
for value in d.values():
     print([value])


print (len(d))
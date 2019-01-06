import json

dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female'  , 'Employee' : 'NA'}
dict3 = {'Sex1': 'female1'}
dict.update(dict2)
dict.update(dict3)
print("Value : %s" %  dict)


x = {'name': 'book2', 'price': 450, 'isbn': 9553849872}

print(json.dumps(x))
import json
import pandas as pd

with open('./person.json', 'r') as file:
        data = json.load(file)


name = input("Please enter a name:")
age = input("Please enter an age:")
city = input("Please enter a city:")

dict = {}
dict["name"] = name
dict["age"] = age
dict["city"] = city

data.append(dict)

with open('./person.json', 'w') as file:
	json.dump(data, file)


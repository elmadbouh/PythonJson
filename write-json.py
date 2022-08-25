import json

list = [{"name":"Adil",
"age":"45",
"city":"Frankfurt"
}]

with open('./person.json','w') as file:
	json.dump(list, file)

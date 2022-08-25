import json
import pandas as pd

with open('./person.json', 'r') as file:
	data = json.load(file)

#print(data)
df = pd.DataFrame(data)
print(df)

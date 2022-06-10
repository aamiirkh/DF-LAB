import json 

f = open('instances.json', "r")
s = f.read()
s = s.replace('\n','')
s = s.replace(',}','}')
data = json.loads(s)
for i in data:
	for j in data[i]:
		print(data[i][j])
	print("\n")
f.close()

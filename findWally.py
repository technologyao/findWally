import json 

file = open ('client.json')
data = json.load(file)



print('Author:',data['News'][0]['Detail']['Author'])
print('Tags:',data['News'][1]['Tags'][1])



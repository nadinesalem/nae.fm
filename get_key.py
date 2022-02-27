import json
dict1={}
dict2={}

def getKey(service,var):
    f = open(f'{service}.json')
    data = json.load(f)
    return data[var]

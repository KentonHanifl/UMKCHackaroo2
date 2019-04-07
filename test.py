import json
from pprint import pprint

with open('full_format_recipes.txt') as json_file:  
    data = json.load(json_file)

def fun(q):
    ret = []
    count = 0
    for recipe in data:
        if count >= 3:
            break
        try:
            if q in recipe['title'].lower():
                ret.append(recipe['title'])
                count +=1
        except KeyError:
            pass #just an empty recipe, don't pay attention
    return ret

q = input('query')
while 'quit' not in q:
    print(fun(q))
    q = input('query')
    

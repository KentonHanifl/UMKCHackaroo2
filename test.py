import json
from pprint import pprint

with open('full_format_recipes.txt') as json_file:  
    data = json.load(json_file)

def query(q):
    #queries for the first recipe with the query string in its title
    for recipe in data:
        try:
            if q in recipe['title']:
                return recipe
        except KeyError:
            pass #just an empty recipe, don't pay attention



def query2(q):
    #queries for the first recipe with the query string in its title
    for recipe in data:
        try:
            if q in recipe['title']:
                print(recipe)
                break
        except KeyError:
            pass #just an empty recipe, don't pay attention

q= 'chicken'

for recipe in data:
    try:
        if q in recipe['title']:
            print(recipe)
            break
        else:
            print(recipe['title'])
    except KeyError:
        pass #just an empty recipe, don't pay attention

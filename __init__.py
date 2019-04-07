from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import json

class FoodRecepiesSkill(MycroftSkill):

    def __init__(self):
        super(FoodRecepiesSkill, self).__init__(name="FoodRecepiesSkill")
        
        #TODO write the full path (?)
        with open('full_format_recipes.txt') as json_file:  
            self.data = json.load(json_file)

        self.recipe = " no recipes found yet"
        
    @intent_file_handler('Recipe.intent')
    def handle_getrecipies_intent(self, message):
        utt = message.data
        q = utt.replace('get me a recipe for ','')

        #save the top 3 responses
        self.recipe = self.query(q)
        
        speakstring = "I found a recepie for recipes for " + self.recipe + "say Hey MyCroft tell me the ingredients to get the ingredients or Hey MyCroft tell me the recipe to get the recipe"
        
        self.speak(speakstring)
        

    @intent_file_handler('Ingredients.intent')
    def handle_ingredients_intent(self, message):
        ingredients = self.recipe['ingredients']
        for ingredient in ingredients:
            self.speak(ingredient)

    @intent_file_handler('Directions.intent')
    def handle_recipe_intent(self, message):
        recipe = self.recipe['directions']
        for step in recipe:
            self.speak(step)
    
    def stop(self):
        return False

    def query(q):
    #queries for the first recipe with the query string in its title
    for recipe in data:
        try:
            return recipe
        except KeyError:
            pass #just an empty recipe, don't pay attention

def create_skill():
    return TemplateSkill()

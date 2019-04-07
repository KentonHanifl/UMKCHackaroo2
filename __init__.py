from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_file_handler
from mycroft.util.log import LOG
import json

class FoodRecipiesSkill(MycroftSkill):

    def __init__(self):
        super(FoodRecipiesSkill, self).__init__(name="FoodRecipiesSkill")
        
        #TODO write the full path (?)
        with open('/home/pi/skills/umkchackaroo2.kentonschool/full_format_recipes.txt') as json_file:  
            self.data = json.load(json_file)

        self.recipe = " no recipes found yet"
        
    @intent_file_handler('Recipe.intent')
    def handle_getrecipies_intent(self, message):
        utt = message.data.get('utterance')
        try:
            q = utt.replace('recipe for ','')

            #save the top 3 responses
            self.recipe = self.query(q)
            
            speakstring = "I found a recepie for " + self.recipe['title'] + ". say Hey MyCroft tell me the ingredients to get the ingredients or Hey MyCroft tell me the recipe to get the recipe"
            
            self.speak(speakstring)
        except:
            self.speak("i couldn't find a recepie. sorry.")
        

    @intent_file_handler('Ingredients.intent')
    def handle_ingredients_intent(self, message):
        try:
            ingredients = self.recipe['ingredients']
            for ingredient in ingredients:
                self.speak(ingredient)
        except:
            self.speak("i don't have any recipe to read ingredients for.")

    @intent_file_handler('Directions.intent')
    def handle_recipe_intent(self, message):
        try:
            recipe = self.recipe['directions']
            for step in recipe:
                self.speak(step)
        except:
            self.speak("i don't have any recipe to read.")
    
    def stop(self):
        return False

    def query(self, q):
        #queries for the first recipe with the query string in its title
        for recipe in self.data:
            try:
                if q in recipe['title'].lower():
                    return recipe
            except KeyError:
                pass #just an empty recipe, don't pay attention

def create_skill():
    return FoodRecipiesSkill()

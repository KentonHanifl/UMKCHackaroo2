## Recipe Getter
Fetches a recipe for the user and reads the recipe's ingredients and steps on request.   

We use a recipe database taken from [this kaggle link](https://www.kaggle.com/hugodarwood/epirecipes#epi_r.csv)  

## Commands
### Get a recipe

This command will have MyCroft search a pre-downloaded database for a recipe with a user specified search string in the title.

* "Recipe for {recipe}"

{recipe} can be any kind of recipe the user asks for. I.E. "MyCroft, recipe for chicken" will find a recipe with chicken in the title

### Read ingredients

* "Tell me the ingredients"

MyCroft will read out the ingredients for whatever recipe he just looked up.

### Read recipe

* "Tell me the recipe

MyCroft will read out the steps for whatever recipe he just looked up.

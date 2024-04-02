from typing import List, Optional
from model import Recipe, Ingredient, NutritionalInfo
import json




RECIPES_JSON_FILE = "recipes.json"


def load_recipes() -> List[Recipe]:
    try:
        with open(RECIPES_JSON_FILE, "r") as file:
            recipes = json.load(file)
            return [Recipe(**recipe) for recipe in recipes]
    except FileNotFoundError:
        return []
    
def save_recipes(recipes: List[Recipe]) -> None:
    existing_recipes = load_recipes()
    all_recipes = existing_recipes + recipes
    with open(RECIPES_JSON_FILE, "w") as file:
        json.dump([recipe.model_dump() for recipe in all_recipes], file)



# Save recipes to JSON file
def save_recipes(recipes: List[Recipe]) -> None:
    with open("recipes.json", "w") as file:
        json.dump([recipe.model_dump() for recipe in recipes], file)


# Get all recipes
def get_recipes() -> List[Recipe]:
    return load_recipes()


# Get recipe by title
def get_recipe_by_title(title: str) -> Optional[Recipe]:
    recipes = load_recipes()
    for recipe in recipes:
        if recipe.title == title:
            return recipe
    return None


# Create a new recipe
def create_recipe(recipe: Recipe) -> Recipe:
    recipes = load_recipes()
    recipes.append(recipe)
    save_recipes(recipes)
    return recipe


# Update an existing recipe
def update_recipe(title: str, updated_recipe: Recipe) -> Optional[Recipe]:
    recipes = load_recipes()
    for i, recipe in enumerate(recipes):
        if recipe.title == title:
            recipes[i] = updated_recipe
            save_recipes(recipes)
            return updated_recipe
    return None


# Delete a recipe
def delete_recipe(title: str) -> Optional[Recipe]:
    recipes = load_recipes()
    for i, recipe in enumerate(recipes):
        if recipe.title == title:
            del recipes[i]
            save_recipes(recipes)
            return recipe
    return None

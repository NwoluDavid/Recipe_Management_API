from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from model import Recipe, Responses
from service import (
    get_recipes,
    get_recipe_by_title,
    create_recipe,
    update_recipe,
    delete_recipe,
)

app = FastAPI()


@app.get("/recipes/", response_model=list[Recipe])
def read_recipes():
    return get_recipes()


@app.get("/recipes/{title}", response_model=Recipe)
def read_recipe(title: str):
    recipe = get_recipe_by_title(title)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@app.post("/recipes/", response_model=Responses)
def create_new_recipe(recipe: Recipe):
    results = create_recipe(recipe).model_dump()
    return JSONResponse (status_code = 201, content ={"data":results, "message": "Recipe created successfully"})



@app.put("/recipes/{title}", response_model=Recipe)
def update_existing_recipe(title: str, recipe: Recipe):
    updated_recipe = update_recipe(title, recipe)
    if updated_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return updated_recipe


@app.delete("/recipes/{title}")
def delete_existing_recipe(title: str):
    deleted_recipe = delete_recipe(title)
    if deleted_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Recipe deleted successfully"}
import json
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_recipes():
    response = client.get("/recipes/")
    assert response.status_code == 200
    recipes = response.json()
    for recipe in recipes:
        assert isinstance(recipe["title"], str)
        assert isinstance(recipe["description"], str)
        assert isinstance(recipe["cooking_instructions"], str)
        assert isinstance(recipe["ingredients"], list)
        for ingredient in recipe["ingredients"]:
            assert isinstance(ingredient["name"], str)
            assert isinstance(ingredient["quantity"], int)
        assert isinstance(recipe["nutritional_info"], dict)
        assert isinstance(recipe["nutritional_info"]["calories"], int)
        assert isinstance(recipe["nutritional_info"]["fat"], int)
        assert isinstance(recipe["nutritional_info"]["protein"], int)

def test_create_new_recipe():
    new_recipe = {
        "title": "Test Recipe",
        "description": "Test Description",
        "cooking_instructions": "Test Instructions",
        "ingredients": [{"name": "Ingredient 1", "quantity": 100}],
        "nutritional_info": {"calories": 100, "fat": 50, "protein": 20}
    }
    response = client.post("/recipes/", json=new_recipe)
    assert response.status_code == 200
    assert response.json()["title"] == new_recipe["title"]

def test_read_recipe():
    response = client.get("/recipes/Test Recipe")
    assert response.status_code == 200
    recipe = response.json()
    assert isinstance(recipe["title"], str)
    assert isinstance(recipe["description"], str)
    assert isinstance(recipe["cooking_instructions"], str)
    assert isinstance(recipe["ingredients"], list)
    for ingredient in recipe["ingredients"]:
        assert isinstance(ingredient["name"], str)
        assert isinstance(ingredient["quantity"], int)
    assert isinstance(recipe["nutritional_info"], dict)
    assert isinstance(recipe["nutritional_info"]["calories"], int)
    assert isinstance(recipe["nutritional_info"]["fat"], int)
    assert isinstance(recipe["nutritional_info"]["protein"], int)

def test_update_recipe():
    updated_recipe = {
        "title": "Test Recipe",
        "description": "Updated Description",
        "cooking_instructions": "Updated Instructions",
        "ingredients": [{"name": "Ingredient 2", "quantity": 200}],
        "nutritional_info": {"calories": 200, "fat": 100, "protein": 40}
    }
    response = client.put("/recipes/Test Recipe", json=updated_recipe)
    assert response.status_code == 200
    assert response.json()["description"] == "Updated Description"

def test_delete_recipe():
    response = client.delete("/recipes/Test Recipe")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Recipe"


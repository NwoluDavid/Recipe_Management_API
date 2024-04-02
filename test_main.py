from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_recipes():
    response = client.get("/recipes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_recipe():
    response = client.get("/recipes/Greek Salad")
    assert response.status_code == 200
    assert response.json()["title"] == "Greek Salad"


def test_read_recipe_not_found():
    response = client.get("/recipes/Nonexistent Recipe")
    assert response.status_code == 404


def test_create_recipe():
    new_recipe = {
        "title": "Test Recipe",
        "description": "Test Description",
        "cooking_instructions": "Test Cooking Instructions",
        "ingredients": [{"name": "Test Ingredient", "quantity": 1}],
        "nutritional_info": {"calories": 100, "fat": 5, "protein": 10}
    }
    response = client.post("/recipes/", json=new_recipe)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Recipe"


def test_update_recipe():
    updated_recipe = {
        "title": "Test Recipe",
        "description": "Updated Description",
        "cooking_instructions": "Updated Cooking Instructions",
        "ingredients": [{"name": "Test Ingredient", "quantity": 1}],
        "nutritional_info": {"calories": 150, "fat": 7, "protein": 12}
    }
    response = client.put("/recipes/Test Recipe", json=updated_recipe)
    assert response.status_code == 200
    assert response.json()["description"] == "Updated Description"


def test_update_recipe_not_found():
    updated_recipe = {
        "title": "Nonexistent Recipe",
        "description": "Updated Description",
        "cooking_instructions": "Updated Cooking Instructions",
        "ingredients": [{"name": "Test Ingredient", "quantity": 1}],
        "nutritional_info": {"calories": 150, "fat": 7, "protein": 12}
    }
    response = client.put("/recipes/Nonexistent Recipe", json=updated_recipe)
    assert response.status_code == 404


def test_delete_recipe():
    response = client.delete("/recipes/Test Recipe")
    assert response.status_code == 200
    assert response.json()["message"] == "Recipe deleted successfully"


def test_delete_recipe_not_found():
    response = client.delete("/recipes/Nonexistent Recipe")
    assert response.status_code == 404


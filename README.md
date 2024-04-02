# Recipe Management API

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Author: Nwolu David

## Overview

The Recipe Management API is a FastAPI-based application designed to simplify the management of recipes. It provides endpoints to perform CRUD (Create, Read, Update, Delete) operations on recipes. With this API, users can retrieve recipes, add new recipes, update existing recipes, and delete recipes from the database.

## Features

- **Retrieve Recipes**: Get a list of all available recipes or retrieve a specific recipe by its title.
- **Add New Recipes**: Create and add new recipes to the database.
- **Update Recipes**: Modify existing recipes with new information.
- **Delete Recipes**: Remove recipes from the database.

## Installation

To install and run the Recipe Management API locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/NwoluDavid/Recipe_Management_API
   cd https://github.com/NwoluDavid/Recipe_Management_API
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

4. Access the API at `http://localhost:8000` in your browser or using API client tools like Postman.

## API Endpoints

- **GET /recipes/**
  - Description: Retrieve all recipes.
  - Response: List of recipes in JSON format.

- **GET /recipes/{title}**
  - Description: Retrieve a specific recipe by its title.
  - Response: Details of the requested recipe in JSON format.

- **POST /recipes/**
  - Description: Add a new recipe.
  - Request Body: JSON data representing the new recipe.
  - Response: Details of the newly created recipe in JSON format.

- **PUT /recipes/{title}**
  - Description: Update an existing recipe by its title.
  - Request Body: JSON data with updated information for the recipe.
  - Response: Details of the updated recipe in JSON format.

- **DELETE /recipes/{title}**
  - Description: Delete a recipe by its title.
  - Response: Confirmation message indicating successful deletion.

## Usage Example

```bash
# Retrieve all recipes
curl http://localhost:8000/recipes/

# Retrieve a specific recipe by title
curl http://localhost:8000/recipes/Greek%20Salad

# Add a new recipe
curl -X POST -H "Content-Type: application/json" -d '{"title": "New Recipe", "description": "Sample description", "cooking_instructions": "Sample instructions", "ingredients": [{"name": "Ingredient 1", "quantity": 1}], "nutritional_info": {"calories": 100, "fat": 5, "protein": 10}}' http://localhost:8000/recipes/

# Update an existing recipe
curl -X PUT -H "Content-Type: application/json" -d '{"title": "New Recipe", "description": "Updated description", "cooking_instructions": "Updated instructions", "ingredients": [{"name": "Ingredient 1", "quantity": 2}], "nutritional_info": {"calories": 150, "fat": 7, "protein": 12}}' http://localhost:8000/recipes/New%20Recipe

# Delete a recipe
curl -X DELETE http://localhost:8000/recipes/New%20Recipe
```

## Test Reports

### Pytest Report

```
pytest test_main.py
================================================================= test session starts =================================================================
platform linux -- Python 3.12.1, pytest-8.1.1, pluggy-1.4.0
rootdir: /home/david/Recipe_Management
configfile: pyproject.toml
plugins: cov-5.0.0, anyio-4.3.0
collected 8 items                                                                                                                                     

test_main.py ........                                                                                                                           [100%]

================================================================== warnings summary ===================================================================
.venv/lib/python3.12/site-packages/pydantic/_internal/_config.py:272
  /home/david/Recipe_Management/.venv/lib/python3.12/site-packages/pydantic/_internal/_config.py:272: PydanticDeprecatedSince20: Support for class-based `config` is deprecated, use ConfigDict instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.6/migration/
    warnings.warn(DEPRECATION_MESSAGE, DeprecationWarning)

.venv/lib/python3.12/site-packages/pydantic/_internal/_config.py:322
  /home/david/Recipe_Management/.venv/lib/python3.12/site-packages/pydantic/_internal/_config.py:322: UserWarning: Valid config keys have changed in V2:
  * 'orm_mode' has been renamed to 'from_attributes'
    warnings.warn(message, UserWarning)

.venv/lib/python3.12/site-packages/httpx/_client.py:680
  /home/david/Recipe_Management/.venv/lib/python3.12/site-packages/httpx/_client.py:680: DeprecationWarning: The 'app' shortcut is now deprecated. Use the explicit style 'transport=WSGITransport(app=...)' instead.
    warnings.warn(message, DeprecationWarning)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================================================ 8 passed, 3 warnings in 1.08s ==================

```

### Pytest Coverage Report

```
pytest --cov
================================================================= test session starts =================================================================
platform linux -- Python 3.12.1, pytest-8.1.1, pluggy-1.4.0
rootdir: /home/david/Recipe_Management
configfile: pyproject.toml
plugins: cov-5.0.0, anyio-4.3.0
collected 8 items                                                                                                                                     

test_main.py ........                                                                                                                           [100%]

================================================================== warnings summary ===================================================================
.venv/lib/python3.12/site-packages/pydantic/_internal/_config.py:272
  /home/david/Recipe_Management/.venv/lib/python3.12/site-packages/pydantic/_internal/_config.py:272: PydanticDeprecatedSince20: Support for class-based `config` is deprecated, use ConfigDict instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.6/migration/
    warnings.warn(DEPRECATION_MESSAGE, DeprecationWarning)

.venv/lib/python3.12/site-packages/pydantic/_internal/_config.py:322
  /home/david/Recipe_Management/.venv/lib/python3.12/site-packages/pydantic/_internal/_config.py:322: UserWarning: Valid config keys have changed in V2:
  * 'orm_mode' has been renamed to 'from_attributes'
    warnings.warn(message, UserWarning)

.venv/lib/python3.12/site-packages/httpx/_client.py:680
  /home/david/Recipe

_Management/.venv/lib/python3.12/site-packages/httpx/_client.py:680: DeprecationWarning: The 'app' shortcut is now deprecated. Use the explicit style 'transport=WSGITransport(app=...)' instead.
    warnings.warn(message, DeprecationWarning)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================================================ 8 passed, 3 warnings in 3.16s 


```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


🎉 Congratulations on discovering the Recipe Management API! 🍽️ Whether you're a cooking enthusiast or a developer looking to streamline recipe management, you're in for a treat! Enjoy exploring the features and creating delicious recipes with ease. Cheers to culinary adventures ahead! 🥳
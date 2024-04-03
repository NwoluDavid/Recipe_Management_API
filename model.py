from typing import Optional
from pydantic import BaseModel, Field


class NutritionalInfo(BaseModel):
    calories: float = Field(None, ge=-1, le=2000, description="amount of calories the recipe contains", examples=[200.00])
    fat: float = Field(None, ge=-1, le=2000, description="amount of fat the recipe contains", examples=[250.00])
    protein: float =  Field( None, ge=-1, le=2000 , description="amount of protein the recipe contains", examples=[20.00])


class Ingredient(BaseModel):
    name: str = Field(min_length=3, max_length=50, description="Name of the ingredient", examples=["Tomatos"], pattern= "^[a-zA-Z ,.'\-\s]+$")
    quantity: int = Field(None, ge=-1, le=2000, description="quantity of the ingredient in kg", examples=[25])


class Recipe(BaseModel):
    title: str = Field(min_length=3, max_length=50, description="Title of the recipe", examples=["Pescadillas "], pattern= "^[a-zA-Z ,.'\-\s]+$")
    description: str  = Field(min_length=3, max_length=1000, description="details about the recipe", examples=[" Pescadillas is a traditional Mexican dish, originally from Acapulco "], pattern="^[a-zA-Z ,.'\-\s]+$")
    cooking_instructions: str = Field(min_length=3, max_length=200000, description="Cookind instructions of the recipe", examples=[" Heat the vegetable oil in a Dutch pan or cast-iron skillet. When the oil is hot and registers at 350 F on a thermometer, add the pescadillas. Fry for about 2 to 3 minutes, until they are golden brown on each side"])
    ingredients:list[Ingredient]
    nutritional_info: Optional[NutritionalInfo]

    class Config:
        orm_mode = True

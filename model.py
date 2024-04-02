from typing import Optional
from pydantic import BaseModel


class NutritionalInfo(BaseModel):
    calories: float
    fat: float
    protein: float


class Ingredient(BaseModel):
    name: str
    quantity: int


class Recipe(BaseModel):
    title: str
    description: str
    cooking_instructions: str
    ingredients:list[Ingredient]
    nutritional_info: Optional[NutritionalInfo]

    class Config:
        orm_mode = True

"""Calculator Package."""

from .coefs import coef_breed, coef_gender


def get_cat_cost(gender: str, breed: str, weight_kg: int) -> int:
    """
    Calculate the cost of a cat based on its gender, breed, and weight.

    Args:
        gender (str): The gender of the cat.
        breed (str): The breed of the cat.
        weight_kg (int): The weight of the cat in kilograms.

    Returns:
        int: The calculated cost of the cat.
    """
    return coef_gender(gender) * coef_breed(breed) * weight_kg

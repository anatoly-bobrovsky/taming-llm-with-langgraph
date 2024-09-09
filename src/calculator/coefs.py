"""Coefficients' functions."""


def coef_gender(gender: str) -> int:
    """
    Return a coefficient based on the gender.

    Args:
        gender (str): The gender of the subject. Expected values are "male" or any other string.

    Returns:
        int: Returns 1 if the gender is "male", otherwise returns 2.
    """
    if gender.lower() == "male":
        return 1
    else:
        return 2


def coef_breed(breed: str) -> int:
    """
    Return a coefficient based on the breed.

    Args:
        breed (str): The breed of the subject.

    Returns:
        int: Returns 10 for "siamese", 20 for "ragdoll", 15 for "abyssinian", and 1 for any other breed.
    """
    match breed.lower():
        case "siamese":
            return 10
        case "ragdoll":
            return 20
        case "abyssinian":
            return 15
        case _:
            return 1

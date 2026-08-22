"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the bake time remaining.

    Parameters:
        number_of_layers (int): The number of layers.

    Returns:
        int: The required preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers that need to be prepared and returns the time (in minutes)
    spent preparing the layers. It is based on the 'PREPARATION_TIME'.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    Parameters:
        number_of_layers (int):the number of layers added to the lasagna.
        elapsed_bake_time (int): the number of minutes the lasagna has spent baking in the oven already.

    Returns:
        int: Returns the total amount of minutes spent in kitchen cooking.

    Function that takes the number of layers of the lasagna and the number of minutes spent baking the lasagna
    and returns the total time spent in kitchen cooking. The time spent preparing the layers is computed using
    'preparation_time_in_minutes' function.
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)

"""
Work out compound interest on a daily basis.

- https://www.mathsisfun.com/money/compound-interest.html
- Don't round() too early, otherwise numbers will be off
- Test on: http://pythontutor.com/
- Type hinting: https://www.jetbrains.com/help/pycharm/type-hinting-in-pycharm.html
"""

from typing import Union


def convert_percentage(percentage: Union[int, float]) -> float:
    """
    Converts a percentage point to a decimal float.

    :param percentage: 1
    :return: 0.1
    """
    return percentage / 100


def whole_percentage(percentage):
    """
    Add 1 to the decimal percentage.
    
    :param percentage: 0.1
    :return: 1.1
    """
    return 1 + convert_percentage(percentage)


def calculate_interest(original_amount, interest):
    """
    Calculates the new amount with interest.

    :param original_amount: 100
    :param interest: 1
    :return: 1.0
    """
    return original_amount * convert_percentage(interest)


def compound_interest_simple(original_amount, interest, days):
    """
    A simplified compound calculation using exponents.

    :param original_amount: 100
    :param interest: 1
    :param days: 30
    :return: 134.78
    """
    return round(original_amount * whole_percentage(interest) ** days, 2)


def compound_interest_recursive(original_amount, interest, days):
    """
    Calculates compounded interest for the number of days given.

    :param original_amount: 100
    :param interest: 1
    :param days: 30
    :return: 134.78
    """
    total = original_amount + calculate_interest(original_amount, interest)

    # TODO `days > 0` runs one too many times, is there a better way?
    if days > 1:
        return compound_interest_recursive(total, interest, days - 1)
    return round(total, 2)


print(str(compound_interest_simple(100, 1, 30)))
print(str(compound_interest_recursive(100, 1, 30)))
print(f'{convert_percentage(2)}')
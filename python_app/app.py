"""
This script was created to test a CI pipeline
"""

def add_one_to_input(number: int):
    """
    Adds 1 to the number given as input

    Arguments:
        number (int): number to which we will add 1.
    """
    return number + 1

def subtract_one_to_input(number: int):
    """
    Subtracts 1 to the number given as input

    Arguments:
        number (int): number to which we will subtract 1.
    """
    return number - 1

if __name__ == '__main__':
    MY_NUMBER = 5
    print("add_one_to_input", add_one_to_input(MY_NUMBER))
    print("subtract_one_to_input", subtract_one_to_input(MY_NUMBER))

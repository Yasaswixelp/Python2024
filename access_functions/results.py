# main.py
# Run through terminal > python -m access_functions.results
from Add_Function.add import math_operations


def my_functions():
    result = math_operations(5, 3)
    print(f"The result is: {result}")


if __name__ == "__main__":
    my_functions()

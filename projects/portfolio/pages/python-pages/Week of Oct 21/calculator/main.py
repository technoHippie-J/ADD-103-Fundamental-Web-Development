"""

    demonstrate the use of the calculator package

"""


from math_operations import calculator
from math_operations import geometry


def main():
    print()

    result = calculator.add(5, 3)
    print("Addition result:", result)

    result = calculator.subtract(10, 4)
    print("Subtraction result:", result)

    result = geometry.area_rect(5, 3)
    print("Rectangle area:", result)

    result = geometry.area_tri(5, 3)
    print("Triangle area:", result)

    result = geometry.area_circ(5)
    print("Circle area:", result)

    print()


main()

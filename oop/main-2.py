# main.py

from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    # Create a list of shapes (Rectangle and Circle)
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Iterate through the shapes and print their areas
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
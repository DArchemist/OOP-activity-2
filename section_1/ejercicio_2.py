import math

class EquilateralTriangle:
    # First we define the variables3

    side: float

    # Then we create a constructor method to assign the side to the EquilateralTriangle object

    def __init__(self, side: float):
        self.side = side

    # Finally, we create methods to compute the perimeter, the height, and the area of the triangle

    def get_perimeter(self) -> float:
        return 3 * self.side
    
    def get_height(self) -> float:
        return math.sqrt(3) * self.side / 2

    def get_area(self) -> float:
        return self.side * self.get_height() / 2


# To test the code, do

if __name__ == "__main__":
    triangle = EquilateralTriangle(float(input('INGRESE EL LADO DEL TRIÁNGULO EQUILÁTERO: ')))
    print(f'EL PERÍMETRO, LA ALTURA, Y EL ÁREA DEL TRIÁNGULO EQUILÁTERO CON LADO {triangle.side:.2f} SON {triangle.get_perimeter():.2f}, {triangle.get_height():.2f}, Y {triangle.get_area():.2f}, RESPECTIVAMENTE.')
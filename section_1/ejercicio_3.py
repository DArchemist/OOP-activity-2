import math

class Triangle:
    # First we define the variables

    side_1: float
    side_2: float
    side_3: float

    # Then we create a constructor method to assign the sides to the Triangle object

    def __init__(self, side_1: float, side_2: float, side_3: float):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    # Finally, we create methods to compute the perimeter, the semiperimeter, and the area of the triangle

    def get_perimeter(self) -> float:
        return self.side_1 + self.side_2 + self.side_3
    
    def get_semiperimeter(self) -> float:
        return self.get_perimeter() / 2

    def get_area(self) -> float:
        semiperimeter = self.get_semiperimeter()
        return math.sqrt(semiperimeter * (semiperimeter - self.side_1) * (semiperimeter - self.side_2) * (semiperimeter - self.side_3))


# To test the code, do

if __name__ == "__main__":
    triangle = Triangle(float(input('INGRESE EL PRIMER LADO DEL TRIÁNGULO: ')), float(input('INGRESE EL SEGUNDO LADO DEL TRIÁNGULO: ')), float(input('INGRESE EL TERCER LADO DEL TRIÁNGULO: ')))
    print(f'EL PERÍMETRO, EL SEMIPERÍMETRO, Y EL ÁREA DEL TRIÁNGULO CON LADOS {triangle.side_1:.2f}, {triangle.side_2:.2f}, Y {triangle.side_3:.2f} SON {triangle.get_perimeter():.2f}, {triangle.get_semiperimeter():.2f}, Y {triangle.get_area():.2f}, RESPECTIVAMENTE.')
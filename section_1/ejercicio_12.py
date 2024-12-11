import math

class SecondDegreePolynomial:
    A = None
    B = None
    C = None
    roots = None

    def __init__(self, A: float, B: float, C: float):
        self.A = A
        self.B = B
        self.C = C

    def _compute_determinant(self) -> float:
        return self.B ** 2 - 4 * self.A * self.C
    
    def get_roots(self) -> tuple[any]:
        determinant = self._compute_determinant()
        if math.isclose(0, determinant, rel_tol=1e-9, abs_tol=1e-9):
            root = - self.B / (2 * self.A)
            return (root, root)
        elif determinant > 0:
            root_1 = (- self.B + math.sqrt(determinant))/ (2 * self.A)
            root_2 = (- self.B - math.sqrt(determinant))/ (2 * self.A)
            return (root_1, root_2)
        else:
            root_1 = complex(- self.B / (2 * self.A), math.sqrt(-determinant) / (2 * self.A))
            root_2 = complex(- self.B / (2 * self.A), - math.sqrt(-determinant) / (2 * self.A))
            return (root_1, root_2)
        

# To test the code, do:

if __name__ == '__main__':
    print(SecondDegreePolynomial(float(input("INSERTE EL PARÁMETRO A: ")), float(input("INSERTE EL PARÁMETRO B: ")), float(input("INSERTE EL PARÁMETRO C: "))).get_roots())
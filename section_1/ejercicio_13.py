class WeightComparator:
    spheres_weights: list[float]

    def __init__(self, spheres_weights: list[float]):
        self.spheres_weights = spheres_weights.copy()

    def get_heavier_sphere(self) -> None:
        if (self.spheres_weights[0] > self.spheres_weights[1]) and (self.spheres_weights[0] > self.spheres_weights[2]):
            print("La ESFERA A ES LA DE MAYOR PESO")
        elif (self.spheres_weights[1] > self.spheres_weights[2]):
             print("La ESFERA B ES LA DE MAYOR PESO")
        else:
             print("La ESFERA C ES LA DE MAYOR PESO")


# To test the code, do:

if __name__ == '__main__':
    WeightComparator([3, 1, 2]).get_heavier_sphere()
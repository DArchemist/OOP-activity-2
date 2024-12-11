class WeightComparator:
    # First we define the variables

    sphere_A_weight: float
    sphere_B_weight: float
    sphere_C_weight: float
    sphere_D_weight: float

    # Then, we define a constructor method for creating a WeightComparator object

    def __init__(self, spheres_weights: list[float]):
        self.sphere_A_weight = spheres_weights[0]
        self.sphere_B_weight = spheres_weights[1]
        self.sphere_C_weight = spheres_weights[2]
        self.sphere_D_weight = spheres_weights[3]

    # Now, we define a method to get the sphere that is different form the other ones

    def get_different_sphere(self) -> None:
        if (self.sphere_A_weight == self.sphere_B_weight) and (self.sphere_A_weight == self.sphere_C_weight):
            message = 'LA ESFERA D ES LA DIFERENTE'
            if (self.sphere_D_weight > self.sphere_A_weight):
                print(f'{message} Y ES LA DE MAYOR PESO')
            else:
                print(f'{message} Y ES LA DE MENOR PESO')
        elif (self.sphere_A_weight == self.sphere_B_weight) and (self.sphere_A_weight == self.sphere_D_weight):
            message = 'LA ESFERA C ES LA DIFERENTE'
            if (self.sphere_C_weight > self.sphere_A_weight):
                print(f'{message} Y ES LA DE MAYOR PESO')
            else:
                print(f'{message} Y ES LA DE MENOR PESO')
        elif (self.sphere_A_weight == self.sphere_C_weight) and (self.sphere_A_weight == self.sphere_D_weight):
            message = 'LA ESFERA B ES LA DIFERENTE'
            if (self.sphere_B_weight > self.sphere_A_weight):
                print(f'{message} Y ES LA DE MAYOR PESO')
            else:
                print(f'{message} Y ES LA DE MENOR PESO')
        elif (self.sphere_B_weight == self.sphere_C_weight) and (self.sphere_B_weight == self.sphere_D_weight):
            message = 'LA ESFERA A ES LA DIFERENTE'
            if (self.sphere_A_weight > self.sphere_B_weight):
                print(f'{message} Y ES LA DE MAYOR PESO')
            else:
                print(f'{message} Y ES LA DE MENOR PESO')


# To test the code, do:

if __name__ == '__main__':
    WeightComparator([1, 1, 1, 12]).get_different_sphere()
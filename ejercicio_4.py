import math

class Comparator:
    @staticmethod
    def compare(number_1: float, number_2: float) -> None:
        epsilon = 1e-9 # We define a tolerance to consider two floats to be equal

        if math.isclose(number_1, number_2, rel_tol=epsilon, abs_tol=epsilon):
            print(f'{number_1} ES IGUAL QUE {number_2}')
        else:
            if number_1 > number_2:
                print(f'{number_1} ES MAYOR QUE {number_2}')
            if number_2 > number_1:
                print(f'{number_1} ES MENOR QUE {number_2}')


# To test the code, do

if __name__ == "__main__":
    Comparator.compare(float(input('INGRESE EL PRIMER NÚMERO: ')), float(input('INGRESE EL SEGUNDO NÚMERO: ')))
class Comparator:
    #First, we define a static method to get the biggest number among three integers
    
    @staticmethod
    def get_biggest_number(number_1: int, number_2: int, number_3: int) -> int:
        if (number_1 > number_2) and (number_1 > number_3):
            return number_1
        else:
            if number_2 > number_3:
                return number_2
            else:
                return number_3
            

# To test the code, do

if __name__ == "__main__":
    number_1 = int(input("INGRESE EL PRIMER NÚMERO: "))
    number_2 = int(input("INGRESE EL SEGUNDO NÚMERO: "))
    number_3 = int(input("INGRESE EL TERCER NÚMERO: "))
    biggest_number = Comparator.get_biggest_number(number_1, number_2, number_3)

    print(f'EL VALOR MAYOR ENTRE {number_1}, {number_2}, Y {number_3} ES: {biggest_number}')
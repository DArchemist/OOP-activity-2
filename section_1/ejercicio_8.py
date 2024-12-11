class Purchase:
    # First we define the variables

    purchase_total: float
    sphere_color: str
    discount: int
    purchase_total_with_discount: float

    # Then, we define a constructor method for creating a Purchase object

    def __init__(self, purchase_total: float, sphere_color: str): 
        self.purchase_total = purchase_total
        self.sphere_color = sphere_color.upper()

    # Now, we define a method to compute the purchase total after the discount

    def compute_purchase_total_with_discount(self) -> object:
        if self.sphere_color == 'BLANCO':
            self.discount = 0
        elif self.sphere_color == 'VERDE':
            self.discount = 10
        elif self.sphere_color == 'AMARILLO':
            self.discount = 25
        elif self.sphere_color == 'AZUL':
            self.discount = 50
        else:
            self.discount = 100
        self.purchase_total_with_discount = self.purchase_total * (1 - self.discount / 100)
        return self
    
    def print_purchase_info(self) -> None:
        print(f'EL CLIENTE DEBE PAGAR: ${self.purchase_total_with_discount:.2f}')


# To test the code, do

if __name__ == "__main__":
    Purchase(543450, "azul").compute_purchase_total_with_discount().print_purchase_info()
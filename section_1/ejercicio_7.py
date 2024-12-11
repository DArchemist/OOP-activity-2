class Employee:
    # First we define the variables
    employees_name: str
    worked_hours: float
    rate: float
    payment: float

    # Then we define a constructor method to create a new Employee object
    
    def __init__(self, employees_name: str, worked_hours: float, rate: float):
        self.employees_name = employees_name.title()
        self.worked_hours = worked_hours
        self.rate = rate

    # Now a method to compute the salary info

    def compute_payment(self) -> object:
        if self.worked_hours > 40:
            extra_hours = self.worked_hours - 40
            if extra_hours > 8:
                extra_extra_hours = extra_hours - 8
                self.payment = 40 * self.rate + 16 * self.rate + 3 * extra_extra_hours * self.rate
            else:
                self.payment = 40 * self.rate + 2 * extra_hours * self.rate
        else:
            self.payment = self.worked_hours * self.rate
        return self

    # Finally, we define a function for printing the payment info

    def print_payment_info(self) -> None:
        print(f'EL TRABAJADOR {self.employees_name} DEVENGÓ ${self.payment:.2f}')


# To test the code, do

if __name__ == '__main__':
    Employee("Elias José", 53, 4000).compute_payment().print_payment_info()
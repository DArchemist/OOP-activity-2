class Employee:
    employees_name = None
    rate = None
    worked_hours = None
    salary = None

    def __init__(self, employees_name: str, rate: float, worked_hours: float):
        self.employees_name = employees_name.title()
        self.rate = rate
        self.worked_hours = worked_hours

    def compute_salary(self) -> object:
        self.salary = self.rate * self.worked_hours
        return self

    def print_employees_info(self) -> None:
        if self.salary > 450000:
            print(f'EL EMPLEADO {self.employees_name} DEVENGÓ ${self.salary:.2f}')
        else:
            print(f'EL EMPLEADO ES {self.employees_name}')


# To test the code, do:

if __name__ == '__main__':
    Employee('Darley Ortiz', 180, 40000).compute_salary().print_employees_info()

    
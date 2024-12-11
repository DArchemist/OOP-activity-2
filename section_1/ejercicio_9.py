class SalesPeriod:
    # First we initizalize the variables
    sales_per_department = None
    sellers_salary = None
    sellers_salary_per_department = None

    def __init__(self, sales_per_department: list[float], sellers_salary: float):
        self.sales_per_department = sales_per_department.copy()
        self.sellers_salary = sellers_salary
        self.sellers_salary_per_department = [self.sellers_salary for i in range(3)]

    def compute_sellers_salary_per_department(self) -> object:
        total_sales = sum(self.sales_per_department)
        sales_percentage = total_sales * 0.33
        if self.sales_per_department[0] > sales_percentage:
            self.sellers_salary_per_department[0] = self.sellers_salary * 1.2
        if self.sales_per_department[1] > sales_percentage:
            self.sellers_salary_per_department[1] = self.sellers_salary * 1.2
        if self.sales_per_department[2] > sales_percentage:
            self.sellers_salary_per_department[2] = self.sellers_salary * 1.2
        return self
    
    def print_salary_info(self) -> None:
        print(f'EL SALARIO DE LOS VENDEDORES DEL DEPARTAMENTO 1 ES: ${self.sellers_salary_per_department[0]:.2f}, EL SALARIO DE LOS VENDEDORES DEL DEPARTAMENTO 2 ES: ${self.sellers_salary_per_department[1]:.2f}, EL SALARIO DE LOS VENDEDORES DEL DEPARTAMENTO 3 ES: ${self.sellers_salary_per_department[2]:.2f}.')
    

# To test the code, do

if __name__ == "__main__":
    SalesPeriod([4200000, 250000, 3300000], 380320).compute_sellers_salary_per_department().print_salary_info()

class Student:
    # First, we define the variables
    BASE_TUITION = 50000
    enrollment_number = None
    students_name = None
    patrimony = None
    estrato_social = None # This goddamn thing is so Colombian, that I just left it untranslated
    tuition = None

    # Then we define a constructor method to create a new Student object
    
    def __init__(self, enrollment_number: int, students_name: str, patrimony: float, estrato_social: int):
        self.enrollment_number = enrollment_number
        self.students_name = students_name
        self.patrimony = patrimony
        self.estrato_social = estrato_social

    # Then, we create a public method to compute the tuition value
    
    def compute_tuition(self) -> object:
        if self.patrimony > 2000000 and self.estrato_social > 3:
            self.tuition = self.BASE_TUITION + 0.03 * self.patrimony
            return self
        self.tuition = self.BASE_TUITION
        return self
    
    def print_students_info(self) -> None:
        print(f'EL ESTUDIANTE CON NÚMERO DE INSCRIPCIÓN {self.enrollment_number}, Y NOMBRE: {self.students_name}, DEBE PAGAR: ${self.tuition}')


if __name__ == "__main__":
    Student(1234, "Darley Ortiz", 1000000, 3).compute_tuition().print_students_info()
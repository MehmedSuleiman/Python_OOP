class Employee:
    def __init__(self, _id: int, first_name: str, second_name: str, salary: int) -> None:
        self.id = _id
        self.first_name = first_name
        self.last_name = second_name
        self.salary = salary

    def get_full_name(self) -> str :
        return f"{self.first_name} {self.last_name}"

    def raise_salary(self, num_increase: int) -> int:
        self.salary += num_increase
        return self.salary

    def get_annual_salary(self) -> int:
        return self.salary* 12


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())

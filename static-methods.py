
class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cook", "Janitor", "Cashier"]
        return position in valid_positions

employee1 = Employee("Alice", "Cook")
employee2 = Employee("Bob", "Janitor")
employee3 = Employee("Patrick", "Cashier")

print(Employee.is_valid_position("Cook"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
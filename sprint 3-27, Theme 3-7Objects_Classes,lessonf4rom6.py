class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days
        self._employee_id = self.__generate_employee_id()

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

    def __generate_employee_id(self):
        return hash(self.first_name + self.second_name + self.gender)

class FullTimeEmployee(Employee):
    def __init__(self, first_name, second_name, gender, salary):
        super().__init__(first_name, second_name, gender)
        self.__salary = salary  # Инициализация защищённого атрибута _salary

    def get_unpaid_vacation(self, start_date, days):
        return f'Начало неоплачиваемого отпуска: {start_date}, продолжительность: {days} дней.'

    def __get_vacation_salary(self):  # Теперь метод является приватным
        return self.__salary * 0.8

class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = self.vacation_days

# Пример использования:
full_time_employee = FullTimeEmployee('Иван', 'Иванов', 'м', 50000)
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
print(f'Зарплата за отпуск: {full_time_employee._get_vacation_salary()}')

part_time_employee = PartTimeEmployee('Анна', 'Петрова', 'ж')
part_time_employee.consume_vacation(5)
print(part_time_employee.get_vacation_details())
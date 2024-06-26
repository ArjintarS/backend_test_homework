class Employee:
    # Атрибут класса, общий для всех экземпляров
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):

        # Атрибуты экземпляра, уникальные для каждого объекта
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender

# Создание экземпляров класса Employee с различными значениями атрибутов
employee1 = Employee("Роберт", "Крузо", "м")
employee2 = Employee("Анна", "Каренина", "ж")

# Вывод информации о сотрудниках
print(f'Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, Пол: {employee1.gender}, Отпускных дней в году: {Employee.vacation_days}.')
print(f'Имя: {employee2.first_name}, Фамилия: {employee2.second_name}, Пол: {employee2.gender}, Отпускных дней в году: {Employee.vacation_days}.')

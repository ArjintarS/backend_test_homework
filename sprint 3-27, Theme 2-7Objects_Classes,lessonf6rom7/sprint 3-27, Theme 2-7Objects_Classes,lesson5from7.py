class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):

        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, days_spent):
        if days_spent <= self.remaining_vacation_days:
            self.remaining_vacation_days -= days_spent
        else:
            print("Недостаточно дней отпуска для списания.")

    def get_vacation_details(self):
        return f"Остаток отпускных дней: {self.remaining_vacation_days}."


employee = Employee('Роберт', 'Крузо', 'м')
employee.consume_vacation(7)
print(employee.get_vacation_details())

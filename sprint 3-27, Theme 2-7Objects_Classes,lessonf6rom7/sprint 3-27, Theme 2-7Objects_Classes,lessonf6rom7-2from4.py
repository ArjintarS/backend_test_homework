class MushroomsCollector:

    # Список ядовитых грибов
    poisonous_mushrooms = ['мухомор', 'поганка']

    def __init__(self):
        # Инициализация списка грибов для каждого экземпляра класса
        self.mushrooms = []

    def is_poisonous(self, mushroom_name):
        # Проверка, является ли гриб ядовитым
        return mushroom_name.lower() in self.poisonous_mushrooms

    def add_mushroom(self, mushroom_name):
        # Добавление гриба, если он не ядовит
        if not self.is_poisonous(mushroom_name):
            self.mushrooms.append(mushroom_name)
        else:
            print('Нельзя добавить ядовитый гриб')

    def __str__(self):
        # Возвращение перечня грибов через запятую
        return ', '.join(self.mushrooms)

# Пример запуска для самопроверки
collector_1 = MushroomsCollector()
collector_1.add_mushroom('Мухомор')
collector_1.add_mushroom('Подосиновик')
collector_1.add_mushroom('Белый')
print(collector_1)  # Выведет: Подосиновик, Белый

collector_2 = MushroomsCollector()
collector_2.add_mushroom('Лисичка')
print(collector_1)  # Выведет: Подосиновик, Белый
print(collector_2)  # Выведет: Лисичка

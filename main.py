# ЗАДАНИЕ
# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`,
# `age`) и методы (`make_sound()`, `eat()`) для всех животных.

# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые
# наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).

# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает
# список животных и вызывает метод `make_sound()` для каждого животного.

# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию
# о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.

# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь
# специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).


# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации
# о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние"
# между запусками программы.

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food

    def make_sound(self):
        print("Щебетание")

    def eat(self):
        print("Зерно")


class Mammal(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food

    def make_sound(self):
        print("Рык")

    def eat(self):
        print("Мясо")


class Reptile(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food

    def make_sound(self):
        print("Шипение")

    def eat(self):
        print("Кузнечики")


def animal_sound(animals):

    for animal in animals:
         animal.make_sound()

# Создаем список животных и вызываем функцию
animals = [Bird("Воробей", 2, "Зерно"),
           Mammal("Лев", 5, "Мясо"),
           Reptile("Ящерица", 1, "Кузнечики")]

animal_sound(animals)


# Вторая часть задания (п.п. 4-5 и дополнительное)
import pickle

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Сотрудник {employee.name} добавлен в зоопарк.")

    def show_animals(self):
        print(f"Животные в зоопарке {self.name}:")
        for animal in self.animals:
            print(f"{animal.name}, возраст: {animal.age}, еда: {animal.food}")

    def show_employees(self):
        print(f"Сотрудники зоопарка {self.name}:")
        for employee in self.employees:
            print(f"{employee.name}, профессия: {type(employee).__name__}")

    def save_zoo(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Состояние зоопарка {self.name} сохранено в файл {filename}.")

    @staticmethod
    def load_zoo(filename):
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
        print(f"Состояние зоопарка загружено из файла {filename}.")
        return zoo


# Классы сотрудников

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит животное {animal.name} едой {animal.food}.")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит животное {animal.name}.")


# Пример использования
if __name__ == "__main__":
    # Создаем зоопарк
    my_zoo = Zoo("Зоопарк Дружбы")

    # Добавляем животных
    sparrow = Bird("Воробей", 2, "Зерно")
    lion = Mammal("Лев", 5, "Мясо")
    lizard = Reptile("Ящерица", 1, "Кузнечики")

    my_zoo.add_animal(sparrow)
    my_zoo.add_animal(lion)
    my_zoo.add_animal(lizard)

    # Добавляем сотрудников
    zookeeper = ZooKeeper("Анна")
    vet = Veterinarian("Доктор Иван")

    my_zoo.add_employee(zookeeper)
    my_zoo.add_employee(vet)

    # Показать всех животных и сотрудников
    my_zoo.show_animals()
    my_zoo.show_employees()

    # Сотрудники выполняют свои задачи
    zookeeper.feed_animal(lion)
    vet.heal_animal(lizard)

    # Сохранение состояния зоопарка
    my_zoo.save_zoo("zoo_state.pkl")

    # Загрузка состояния зоопарка из файла
    loaded_zoo = Zoo.load_zoo("zoo_state.pkl")
    loaded_zoo.show_animals()
    loaded_zoo.show_employees()


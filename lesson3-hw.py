######################################################
# Золушка
######################################################
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'


class Cinderella(Human):
    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size


class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_cinderella(self, *cinderellas):
        for cinderella in cinderellas:
            if cinderella.foot_size == self.shoe_size:
                return cinderella


prince = Prince('Max', 16, 36)
print(
    prince.find_cinderella(
        Cinderella('Kira', 16, 25),
        Cinderella('Ira', 20, 35),
        Cinderella('Ilona', 22, 36),
        Cinderella('Marta', 23, 42),
    )
)

"""
 Створити клас rectangle
1) об'єкт приймає два параметри - дві сторони х у
2) описати методи арифметичні
  + сума площин двок об'єктів
  - різниця площин
3) логічні оператори:
  == повертає true якщо рівні по площині
  != якщо не рівні
  >, < відповідно
4) len() - сума сторін
"""


class Rectangle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.__area = x * y

    def __add__(self, other):
        return self.__area + other.__area

    def __sub__(self, other):
        return self.__area - other.__area

    def __eq__(self, other):
        return self.__area == other.__area

    def __ne__(self, other):
        return self.__area != other.__area

    def __gt__(self, other):
        return self.__area > other.__area

    def __lt__(self, other):
        return self.__area < other.__area

    def __len__(self):
        return self.x + self.y


rect1 = Rectangle(2, 5)
rect2 = Rectangle(5, 5)
print(rect1 + rect2)
print(rect1 - rect2)
print(rect1 == rect2)
print(rect1 != rect2)
print(len(rect1))

'''
1)Створити пустий list
2)Створити клас Letter
3) створити змінну класу __count.
4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
5) при створені об'єкта __count має збільшуватися на 1
6) має бути метод(метод класу) для виводу __сount
7) має бути метод який записує в наш ліст текст з нашої змінної __text
'''
DB = []


class Letter:
    __count = 0

    def __init__(self):
        self.__text = ''
        Letter.__count += 1

    @classmethod
    def get_count(cls):
        print(cls.__count)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

    def save(self):
        DB.append(self.__text)

    @staticmethod
    def show_db():
        print(DB)


letter = Letter()
letter.text = 'Hello'
letter.save()
letter.text = 'OWU'
letter.save()
Letter.show_db()
letter2 = Letter()
Letter.get_count()

'''
1) написати програму для запису відомостей про пасажирські перевезення
2) перевезення відбувається трьома способами, літаком, машиною, поїздом,
3) дані які треба буде зберігати:
  - вартість квитка(літак, поїзд)
  - кількість пасажирів(машина)
  - час в дорозі(всі)
  - час реєстрації(літак)
  - клас:перший,другий(літак)
  - вартість пального(машина)
  - км(машина)
  - місце: купе,св(поїзд)
4) методи:
  - розрахунок вартості доїзду(машина)
  - загальний час перельоту(літак)
  - порівняти час в дорозі між двома будь якими транспортними засобами(двома об'єктами) - наприклад"літак на 5 годин швидше за поїзд"
  - вивести всі дані про перевезення(поїзд)
'''


class Transport:
    def __init__(self, time):
        self.time = time

    def __eq__(self, other):
        return \
            f'{self.__class__.__name__} быстрее чем {other.__class__.__name__}' \
            if self.time - other.time < 0 else \
            f'{self.__class__.__name__} не быстрее чем {other.__class__.__name__}'


class PlaneTrain(Transport):
    def __init__(self, time, tiket_cost):
        super().__init__(time)
        self.tiket_cost = tiket_cost


class Train(PlaneTrain):
    def __init__(self, time, tiket_cost, sit_class):
        super().__init__(time, tiket_cost)
        self.sit_class = sit_class


class Plaine(PlaneTrain):
    def __init__(self, time, tiket_cost, register_time, sit_class):
        super().__init__(time, tiket_cost)
        self.sit_class = sit_class
        self.register_time = register_time

    def total_time(self):
        return self.register_time + self.time


class Car(Transport):
    def __init__(self, time, passagers_count, patrol_cost_litr, distance):
        super().__init__(time)
        self.distance = distance
        self.patrol_cost_litr = patrol_cost_litr
        self.passagers_count = passagers_count

    def cost_of_travel(self):
        return self.distance / 100 * self.passagers_count


car = Car(100, 2, 20, 1000)
train = Train(50, 100, "lux")
print(car == train)

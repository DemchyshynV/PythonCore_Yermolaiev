# def f(st: int) -> int:
#     return 2


# i = 4
# # print(globals())
# def f():
#     global i
#     i=22
#     # print(locals())
#
# f()
# print(i)
#
# def aa():
#     a = 'a'
#     def bb():
#         nonlocal a
#         print(a)
#     bb()
#
# aa()

# def counter():
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         print(count)
#
#     return wrap
#
#
# counter1 = counter()
# counter2 = counter()
#
# counter1()
# counter1()
# counter2()
# counter1()
# counter1()
# counter1()
# counter2()

#################################################################################

# class User:
#     _count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greeting(self, text):
#         print(f'{text} my name is {self.name}')
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return str(self.__dict__)
#
#
# user = User('Max', 14)
# user.greeting('Hi')
# print(user)

# l = [User('Max',13), User('Kira',20)]
# print(l)
# print(user.count)
# print(User._User__count)
# print(user.count)


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print('this is a car')


# class Radio:
#     def play_music(self):
#         print('la-la-la')
#
#
# class DisselCar(Car, Radio):
#     def __init__(self, brand, model, tnvd):
#         super().__init__(brand, model)
#         self.tnvd = tnvd
#
#     def info(self):
#         print('from dissel car info:')
#
#
# dissel = DisselCar('KIA', 'Cerato', True)
# dissel.info()
# dissel.play_music()

# # import abc
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def perimetr(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
#
# # shape = Shape()
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def perimetr(self):
#         return self.a * 2 + self.b * 2
#
#     def area(self):
#         return self.a * self.b
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimetr(self):
#         return self.a + self.b + self.c
#
#     def area(self):
#         return (self.a * self.b) / 2 * self.c
#
#
# shapes = [Rectangle(2, 4), Triangle(3, 8, 6), Rectangle(7, 3)]
#
# for shape in shapes:
#     print(shape.perimetr())
#     print(shape.area())


# class User:
# __count = 0
#
# def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# # @classmethod
# # def inc_count(cls):
# #     cls.__count+=1
# #     print(cls.__count)
# #
# @staticmethod
# def greeting():
#     print('hello')

# user = User('Max', 15)
#
# User.inc_count()
# User.inc_count()
# User.inc_count()
#
# User.

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'

    def __repr__(self):
        return f'{self.name} {self.age}'

    def __len__(self):
        return 45

    def __add__(self, other):
        return self.age - other.age
    def __sub__(self, other):
        return self.age - other.age

user = User('Max', 13)
user2 = User('Max', 55)
print(len(user))
print(user - user2)

print(user.name)

user.name = 44
print(user.__dict__)


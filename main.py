# # Задание 1
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def __eq__(self, other):
#         return self.radius == other.radius

#     def __gt__(self, other):
#         return self.radius > other.radius

#     def __lt__(self, other):
#         return self.radius < other.radius

#     def __le__(self, other):
#         return self.radius <= other.radius

#     def __ge__(self, other):
#         return self.radius >= other.radius

#     def circumference(self):
#         return 2 * 3.14 * self.radius

# circle1 = Circle(5)
# circle2 = Circle(7)

# print("Радиусы окружностей:")
# print("Круг 1:", circle1.radius)
# print("Круг 2:", circle2.radius)

# print("\nПроверка на равенство радиусов:")
# print("Круг 1 == Круг 2:", circle1 == circle2)

# print("\nСравнение длин окружностей:")
# print("Круг 1 > Круг 2:", circle1.circumference() > circle2.circumference())
# print("Круг 1 < Круг 2:", circle1.circumference() < circle2.circumference())
# print("Круг 1 <= Круг 2:", circle1.circumference() <= circle2.circumference())
# print("Круг 1 >= Круг 2:", circle1.circumference() >= circle2.circumference())

        
        
# # Задание 2
# class Airplane:
#     def __init__(self, model, max_passengers, current_passengers=0):
#         self.model = model
#         self.max_passengers = max_passengers
#         self.current_passengers = current_passengers

#     def __eq__(self, other):
#         return self.model == other.model

#     def __gt__(self, other):
#         return self.max_passengers > other.max_passengers

#     def __lt__(self, other):
#         return self.max_passengers < other.max_passengers

#     def __le__(self, other):
#         return self.max_passengers <= other.max_passengers

#     def __ge__(self, other):
#         return self.max_passengers >= other.max_passengers

#     def __add__(self, passengers):
#         new_passengers = self.current_passengers + passengers
#         if new_passengers <= self.max_passengers:
#             self.current_passengers = new_passengers
#         else:
#             print("Ошибка: Превышено максимальное количество пассажиров!")
#         return self

#     def __sub__(self, passengers):
#         new_passengers = self.current_passengers - passengers
#         if new_passengers >= 0:
#             self.current_passengers = new_passengers
#         else:
#             print("Ошибка: Нельзя иметь отрицательное количество пассажиров!")
#         return self

#     def __iadd__(self, passengers):
#         return self.__add__(passengers)

#     def __isub__(self, passengers):
#         return self.__sub__(passengers)

#     def __str__(self):
#         return f"Модель: {self.model}, Максимальное количество пассажиров: {self.max_passengers}, Количество пассажиров на борту: {self.current_passengers}"


# plane1 = Airplane("Boeing 747", 500)
# plane2 = Airplane("Airbus A380", 853)

# print("Сравнение типов самолетов:")
# print("Самолет 1 == Самолет 2:", plane1 == plane2)

# print("\nСравнение максимального количества пассажиров:")
# print("Самолет 1 > Самолет 2:", plane1 > plane2)
# print("Самолет 1 < Самолет 2:", plane1 < plane2)
# print("Самолет 1 <= Самолет 2:", plane1 <= plane2)
# print("Самолет 1 >= Самолет 2:", plane1 >= plane2)

# print("\nДобавление и удаление пассажиров:")
# print(plane1)
# plane1 += 200
# print(plane1)
# plane1 -= 100
# print(plane1)
# plane2 += 1000








# # Задание 3
# class Flat:
#     def __init__(self, area, price):
#         self.area = area
#         self.price = price

#     def __eq__(self, other):
#         return self.area == other.area

#     def __ne__(self, other):
#         return self.area != other.area

#     def __gt__(self, other):
#         return self.price > other.price

#     def __lt__(self, other):
#         return self.price < other.price

#     def __le__(self, other):
#         return self.price <= other.price

#     def __ge__(self, other):
#         return self.price >= other.price


# flat1 = Flat(100, 200000)
# flat2 = Flat(120, 180000)

# print("Проверка на равенство площадей квартир:")
# print("Квартира 1 == Квартира 2:", flat1 == flat2)

# print("\nПроверка на неравенство площадей квартир:")
# print("Квартира 1 != Квартира 2:", flat1 != flat2)

# print("\nСравнение квартир по цене:")
# print("Квартира 1 > Квартира 2:", flat1 > flat2)
# print("Квартира 1 < Квартира 2:", flat1 < flat2)
# print("Квартира 1 <= Квартира 2:", flat1 <= flat2)
# print("Квартира 1 >= Квартира 2:", flat1 >= flat2) 
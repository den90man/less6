#1#
# from time import sleep
# class TrafficLight:
#     light= ['Красный', 'Желтый', 'Зеленый']
#
#     def running(self):
#         i = 0
#         while i < 3:
#             print(f'Светофор переключается \n ')
#             print(f'{TrafficLight.light[i]}')
#             if i == 0:
#                 sleep(9)
#             elif i == 1:
#                 sleep(4)
#             elif i == 2:
#                 sleep(8)
#             i += 1
# TrafficLight = TrafficLight()
# TrafficLight.running()


#2
# class Road:
#     def __init__(self, _length, _width, _weight, _tall):
#         self._length = _length
#         self._width = _width
#         self._weight = _weight
#         self._tall = _tall
# class Mass(Road):
#
#     def __init__(self, _length, _width, _weight, _tall):
#             super().__init__(_length, _width, _weight, _tall)
#     def get_weight(self):
#         return self._length * self._width * self._weight * self._tall
# m = Mass(12,32, 234, 21)
# print(m.get_weight())

#3
# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
# class Position(Worker):
#
#     def __init__(self, name, surname, position, wage, bonus):
#             super().__init__(name, surname, position, wage, bonus)
#     def get_full_name(self):
#         return self.name+' ' + self.surname
#     def get_total_income(self):
#         return self._income.get('wage') + self._income.get('bonus')
# position = Position('Иван', 'иванов', 'плотник', 20000, 21000)
# print(position.get_full_name())
# print(position.position)
# print(position.get_total_income())
# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}



#4

# class Car:
#     # atributes
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#     def go(self):
#         return f'{self.name} Старт'
#     def stop(self):
#         return f'{self.name} Стоп'
#     def turn_right(self):
#         return f'{self.name} вправо'
#     def turn_left(self):
#         return f'{self.name} влево  '
#     def show_speed(self):
#         return f'Скорость  {self.name} равна  {self.speed}'
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#     def show_speed(self):
#         print(f'Скорость {self.name} равна {self.speed}')
#         if self.speed > 80:
#             return f'Скорость {self.name} превышена'
#         else:
#             return f'Скорость {self.name} в норме'
# class SportCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#     def show_speed(self):
#         print(f'Скорость {self.name} равна {self.speed}')
#         if self.speed > 60:
#             return f'Скорость {self.name} превышена'
#         else:
#             return f'Скорость {self.name} в норме'
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#     def police(self):
#         if self.is_police:
#             return f'{self.name} Милиция'
#
# SportCar = SportCar(10, 'White', 'SportCar', False)
# TownCar = TownCar(30, 'White', 'TownCar', False)
# WorkCar = WorkCar(70, 'White', 'WorkCar', True)
# PoliceCar = PoliceCar(34, 'White',  'PoliceCar', True)
# print(WorkCar.turn_left())
# print(f'При повороте {TownCar.turn_right()}, сиглал для {SportCar.stop()}')
# print(f'{WorkCar.show_speed()}')
# print(f'{WorkCar.name}, цвета {WorkCar.color}')
# print(f'{SportCar.name},{SportCar.is_police}')
# print(f'{WorkCar.name},{WorkCar.is_police}')
# print(SportCar.show_speed())
# print(TownCar.show_speed())
# print(PoliceCar.police())
# print(PoliceCar.show_speed())

#5
# class Stationary:
#     def __init__(self, title):
#         self.title = title
#     def draw(self):
#         return f'Запуск отрисовки: {self.title}'
# class Pen(Stationary):
#     def __init__(self, title):
#         super().__init__(title)
#     def draw(self):
#         return f'{self.title}. Использование ручки'
# class Pencil(Stationary):
#     def __init__(self, title):
#         super().__init__(title)
#     def draw(self):
#         return f'{self.title}. Использование карандаша'
# class Handle(Stationary):
#     def __init__(self, title):
#         super().__init__(title)
#     def draw(self):
#         return f' {self.title}. Использование маркера'
# stay = Stationary('')
# pen = Pen('Ручка')
# pencil = Pencil('Карандаш')
# handle = Handle('Маркер')
# print (stay.draw())
# print(pen.draw())
# print(pencil.draw())
# print(handle.draw())

class Car:
    def drive(self):
        pass

class Sedan(Car):
    def drive(self):
        print("Вождение седана")  # Вывод: Вождение седана

class SUV(Car):
    def drive(self):
        print("Вождение внедорожника")  # Вывод: Вождение внедорожника

class CarFactory:
    def create_car(self, car_type):
        if car_type == "sedan":
            return Sedan()
        elif car_type == "suv":
            return SUV()
        else:
            raise ValueError("Недопустимый тип автомобиля")

# Использование паттерна Фабрика
factory = CarFactory()
car1 = factory.create_car("sedan")
car1.drive()  # Вывод: Вождение седана

car2 = factory.create_car("suv")
car2.drive()  # Вывод: Вождение внедорожника
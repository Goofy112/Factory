class Car:
    def __init__(self):
        self.brand = None
        self.model = None
        self.color = None

    def __str__(self):
        return f"Автомобиль: {self.brand} {self.model}, Цвет: {self.color}"  # Вывод: Автомобиль: Toyota Camry, Цвет: Синий

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_brand(self, brand):
        self.car.brand = brand

    def set_model(self, model):
        self.car.model = model

    def set_color(self, color):
        self.car.color = color

    def get_car(self):
        return self.car

# Использование паттерна Строитель
builder = CarBuilder()
builder.set_brand("Toyota")
builder.set_model("Camry")
builder.set_color("Синий")

car = builder.get_car()
print(car)  # Вывод: Автомобиль: Toyota Camry, Цвет: Синий

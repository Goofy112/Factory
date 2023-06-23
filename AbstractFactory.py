class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()

class AbstractProductA:
    def use(self):
        pass

class AbstractProductB:
    def eat(self):
        pass

class ProductA1(AbstractProductA):
    def use(self):
        print("Использование Продукта A1")  # Вывод: Использование Продукта A1

class ProductA2(AbstractProductA):
    def use(self):
        print("Использование Продукта A2")  # Вывод: Использование Продукта A2

class ProductB1(AbstractProductB):
    def eat(self):
        print("Употребление Продукта B1")  # Вывод: Употребление Продукта B1

class ProductB2(AbstractProductB):
    def eat(self):
        print("Употребление Продукта B2")  # Вывод: Употребление Продукта B2

# Использование паттерна Абстрактная фабрика
factory1 = ConcreteFactory1()
product_a1 = factory1.create_product_a()
product_a1.use()  # Вывод: Использование Продукта A1

product_b1 = factory1.create_product_b()
product_b1.eat()  # Вывод: Употребление Продукта B1

factory2 = ConcreteFactory2()
product_a2 = factory2.create_product_a()
product_a2.use()  # Вывод: Использование Продукта A2

product_b2 = factory2.create_product_b()
product_b2.eat()  # Вывод: Употребление Продукта B2

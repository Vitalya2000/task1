PI = 3.1415926535

'''Не очень понял в условии про библиотеку для поставки внешним клиентам. Я предположил, что это внешний файл с 
классами фигур, который можно использовать не только для подсчета площади определённых фигур, но и для 
создания своих классов фигур, которые будут наследоваться от родительского класса Figure с общим полем a'''


class Figure:
    def __init__(self, a):
        self.a = a

    def area(self):
        pass


class Circle(Figure):
    def __init__(self, a, ):
        super().__init__(a)

    def area(self):
        return PI * self.a ** 2


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__(a)
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        if self.a ** 2 + self.b ** 2 == self.c ** 2:
            print("Треугольник является прямоугольным")
            return self.a * self.b / 2
        else:
            print("Треугольник не является прямоугольным")
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

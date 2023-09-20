import figures


class Rectangle(figures.Figure):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def area(self):
        return self.a * self.b


c = figures.Circle(5)
print(f"S = {c.area()}")
t = figures.Triangle(3, 4, 5)
print(f"S = {t.area()}")
r = Rectangle(5, 6)
print(f"S = {r.area()}")

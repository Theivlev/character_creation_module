from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Вычисляет квадратный корень."""
    if your_number <= 0:
        return
    root = CalculateSquareRoot(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа.'
          'Это будет:', root)


calc(25.5)
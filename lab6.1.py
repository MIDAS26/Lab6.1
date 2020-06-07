'''
Igor Okhman IP-96
Variant 15
'''

import math
from abc import ABC, abstractmethod


class Function(ABC):
    def __init__(self, x, N):
        self.x = x
        self.N = N

    @abstractmethod
    def exponent(self):
        pass

    @abstractmethod
    def ln(self):
        pass


class Exponent(Function):
    def exponent(self):
        exp = 0
        for i in range(N):
            exp += x ** i / math.factorial(i)
        print('e : {}'.format(exp))

    def ln(self):
        pass


class Ln(Function):
    def exponent(self):
        pass

    def ln(self):
        accuracy = 0.000001
        ln_prev = 0
        ln_current = x
        n = 1
        difference = abs(ln_current - ln_prev)
        while difference > accuracy:
            ln_prev += ((-1) ** (n - 1)) * ((x ** n) / n)
            ln_current += ((-1) ** n) * ((x ** (n + 1)) / (n + 1))
            difference = abs(ln_current - ln_prev)
            n += 1
        print('ln : {}'.format(ln_current))


Input = int(input("To choose ln(x) enter 1 \n"
                 "To choose e(x) enter 2 \n"))


if Input == 1:
    x = float(input("Enter x(from -1 to 1):"))
    N = int(input("Enter n: "))
    f1 = Ln(x, N)
    f1.ln()
elif Input == 2:
    x = float(input("Enter x: "))
    N = int(input("Enter n: "))
    f2 = Exponent(x, N)
    f2.exponent()

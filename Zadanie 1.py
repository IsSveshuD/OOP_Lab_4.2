#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Equation:
    def __init__(self, a, b):
        self.first = a
        self.second = b

    def read(self):
        self.first = float(input("Введите значение коэффициента A: "))
        self.second = float(input("Введите значение коэффициента B: "))

    def display(self):
        print(f"Уравнение y = {self.first}x + {self.second}")

    def function(self, x):
        return self.first * x + self.second

    def __str__(self):
        return f"Equation({self.first}, {self.second})"

    def __eq__(self, other):
        if isinstance(other, Equation):
            return self.first == other.first and self.second == other.second
        return False

    def __add__(self, other):
        if isinstance(other, Equation):
            return Equation(self.first + other.first,
                            self.second + other.second)
        elif isinstance(other, (int, float)):
            return Equation(self.first, self.second + other)
        else:
            raise ValueError("Illegal type of the argument")

    def __sub__(self, other):
        if isinstance(other, Equation):
            return Equation(self.first - other.first,
                            self.second - other.second)
        elif isinstance(other, (int, float)):
            return Equation(self.first, self.second - other)
        else:
            raise ValueError("Illegal type of the argument")


if __name__ == "__main__":
    eq1 = Equation(2, 3)
    eq2 = Equation(1, 4)

    print(eq1 + eq2)
    print(eq1 - eq2)
    print(eq1 + 5)
    print(eq1 == eq2)
    print(str(eq1))

import math

class CalculatorModel:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def square_root(self, a):
        """cacule la racine carree d'un nombres"""
        if a < 0:
            raise ValueError("cannot calculate square root of negative number")
        return math.sqrt(a)
    
    def absolute_value(self, a):
        """calcule la valeur absolue d'un nombre"""
        return abs(a)   
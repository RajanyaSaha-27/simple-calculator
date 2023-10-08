import math

class ScientificCalculator:

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    def square_root(self, a):
        return math.sqrt(a)

    def exponentiation(self, a, b):
        return math.pow(a, b)

    def logarithm(self, a, base=10):
        return math.log(a, base)

    def sin(self, a):
        return math.sin(math.radians(a))

    def cos(self, a):
        return math.cos(math.radians(a))

    def tan(self, a):
        return math.tan(math.radians(a))

    def asin(self, a):
        return math.asin(a)

    def acos(self, a):
        return math.acos(a)

    def atan(self, a):
        return math.atan(a)

    def exponent(self, a):
        return math.exp(a)

    def log(self, a, base=math.e):
        return math.log(a, base)

    def get_numbers(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return a, b

    def get_operator(self):
        return input("Enter operator (add, sub, mul, div, sqrt, sin, cos, tan, asin, acos, atan, exp, log, pow): ")

    def calculate(self):
        operator = self.get_operator()

        if operator in ['sqrt', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'exp']:
            a = int(input("Enter the number: "))
            if operator == 'sqrt':
                print(self.square_root(a))
            elif operator == 'sin':
                print(self.sin(a))
            elif operator == 'cos':
                print(self.cos(a))
            elif operator == 'tan':
                print(self.tan(a))
            elif operator == 'asin':
                print(self.asin(a))
            elif operator == 'acos':
                print(self.acos(a))
            elif operator == 'atan':
                print(self.atan(a))
            elif operator == 'exp':
                print(self.exponent(a))
        else:
            a, b = self.get_numbers()
            if operator == 'add':
                print(self.addition(a, b))
            elif operator == 'sub':
                print(self.subtraction(a, b))
            elif operator == 'mul':
                print(self.multiplication(a, b))
            elif operator == 'div':
                print(self.division(a, b))
            elif operator == 'log':
                print(self.log(a, b))
            elif operator == 'pow':
                print(self.exponentiation(a, b))
            else:
                print("Invalid operator")

calc = ScientificCalculator()
calc.calculate()

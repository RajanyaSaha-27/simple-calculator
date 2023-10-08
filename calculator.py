class Calculator:

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    def get_numbers(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return a, b

    def get_operator(self):
        return input("Enter operator (add, sub, mul, div): ")

    def calculate(self):
        a, b = self.get_numbers()
        operator = self.get_operator()

        if operator == 'add':
            print(self.addition(a, b))
        elif operator == 'sub':
            print(self.subtraction(a, b))
        elif operator == 'mul':
            print(self.multiplication(a, b))
        elif operator == 'div':
            print(self.division(a, b))
        else:
            print("Invalid operator")

calc = Calculator()
calc.calculate()
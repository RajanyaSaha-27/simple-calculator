import math
from typing import Union

class ScientificCalculator:
    """
    A scientific calculator class with various mathematical operations.
    """

    def __init__(self):
        self.operators = {
            'add': self.addition,
            'sub': self.subtraction,
            'mul': self.multiplication,
            'div': self.division,
            'sqrt': self.square_root,
            'sin': self.sin,
            'cos': self.cos,
            'tan': self.tan,
            'asin': self.asin,
            'acos': self.acos,
            'atan': self.atan,
            'exp': self.exponent,
            'log': self.logarithm,
            'pow': self.exponentiation
        }

    def addition(self, a: float, b: float) -> float:
        """Return the sum of two numbers."""
        return a + b

    def subtraction(self, a: float, b: float) -> float:
        """Return the difference between two numbers."""
        return a - b

    def multiplication(self, a: float, b: float) -> float:
        """Return the product of two numbers."""
        return a * b

    def division(self, a: float, b: float) -> float:
        """Return the quotient of two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def square_root(self, a: float) -> float:
        """Return the square root of a number."""
        if a < 0:
            raise ValueError("Square root of negative number is undefined.")
        return math.sqrt(a)

    def exponentiation(self, a: float, b: float) -> float:
        """Return the result of raising a to the power of b."""
        return math.pow(a, b)

    def logarithm(self, a: float, base: float = 10) -> float:
        """Return the logarithm of a with the given base."""
        if a <= 0:
            raise ValueError("Logarithm of non-positive number is undefined.")
        return math.log(a, base)

    def sin(self, a: float) -> float:
        """Return the sine of an angle in degrees."""
        return math.sin(math.radians(a))

    def cos(self, a: float) -> float:
        """Return the cosine of an angle in degrees."""
        return math.cos(math.radians(a))

    def tan(self, a: float) -> float:
        """Return the tangent of an angle in degrees."""
        return math.tan(math.radians(a))

    def asin(self, a: float) -> float:
        """Return the arcsine of a number."""
        if abs(a) > 1:
            raise ValueError("Arcsine input must be between -1 and 1.")
        return math.asin(a)

    def acos(self, a: float) -> float:
        """Return the arccosine of a number."""
        if abs(a) > 1:
            raise ValueError("Arccosine input must be between -1 and 1.")
        return math.acos(a)

    def atan(self, a: float) -> float:
        """Return the arctangent of a number."""
        return math.atan(a)

    def exponent(self, a: float) -> float:
        """Return Euler's number raised to the power of a."""
        return math.exp(a)

    def log(self, a: float, base: float = math.e) -> float:
        """Return the logarithm of a with the given base."""
        if a <= 0:
            raise ValueError("Logarithm of non-positive number is undefined.")
        return math.log(a, base)

    def get_number(self, prompt: str) -> float:
        """Get a single number input from the user."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_operator(self) -> str:
        """Get the operator input from the user."""
        while True:
            op = input("Enter operator (add, sub, mul, div, sqrt, sin, cos, tan, asin, acos, atan, exp, log, pow): ").lower()
            if op in self.operators:
                return op
            print("Invalid operator. Please choose one of the available options.")

    def calculate(self) -> None:
        """Perform calculations based on user input."""
        while True:
            operator = self.get_operator()

            if operator in ['sqrt', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'exp']:
                try:
                    a = self.get_number("Enter the number: ")
                    print(f"Result: {self.operators[operator](a)}")
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
            else:
                try:
                    a = self.get_number("Enter first number: ")
                    b = self.get_number("Enter second number: ")
                    print(f"Result: {self.operators[operator](a, b)}")
                except Exception as e:
                    print(f"An error occurred: {str(e)}")

            cont = input("Do you want to continue? (yes/no): ").lower()
            if cont != 'yes':
                break

if __name__ == "__main__":
    calc = ScientificCalculator()
    calc.calculate()

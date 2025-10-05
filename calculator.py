import math
from typing import Callable, Dict


class ScientificCalculator:
    """
    A scientific calculator class with various mathematical operations.
    """

    def __init__(self):
        self.operators: Dict[str, Callable] = {
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
            'pow': self.exponentiation,
            'help': self.show_help,
        }

    # ---------------- Basic Operations ---------------- #

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

    def exponentiation(self, a: float, b: float) -> float:
        """Return a raised to the power of b."""
        return math.pow(a, b)

    def logarithm(self, a: float, base: float = math.e) -> float:
        """Return the logarithm of a with the given base (default: natural log)."""
        if a <= 0:
            raise ValueError("Logarithm of non-positive number is undefined.")
        return math.log(a, base)

    def exponent(self, a: float) -> float:
        """Return e raised to the power of a."""
        return math.exp(a)

    # ---------------- Trigonometric Functions ---------------- #

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
        """Return the arcsine of a number (in degrees)."""
        if abs(a) > 1:
            raise ValueError("Arcsine input must be between -1 and 1.")
        return math.degrees(math.asin(a))

    def acos(self, a: float) -> float:
        """Return the arccosine of a number (in degrees)."""
        if abs(a) > 1:
            raise ValueError("Arccosine input must be between -1 and 1.")
        return math.degrees(math.acos(a))

    def atan(self, a: float) -> float:
        """Return the arctangent of a number (in degrees)."""
        return math.degrees(math.atan(a))

    # ---------------- Misc ---------------- #

    def square_root(self, a: float) -> float:
        """Return the square root of a number."""
        if a < 0:
            raise ValueError("Square root of negative number is undefined.")
        return math.sqrt(a)

    def show_help(self, *_):
        """Show available operators."""
        return "Available operators: " + ", ".join(self.operators.keys())

    # ---------------- User Interaction ---------------- #

    def get_number(self, prompt: str) -> float:
        """Get a number input from the user with validation."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_operator(self) -> str:
        """Get the operator input from the user."""
        while True:
            op = input("Enter operator (type 'help' to list options): ").lower()
            if op in self.operators:
                return op
            print("Invalid operator. Try again or type 'help'.")

    def calculate(self) -> None:
        """Perform calculations based on user input."""
        while True:
            operator = self.get_operator()

            # Single input operations
            if operator in ['sqrt', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'exp']:
                try:
                    a = self.get_number("Enter the number: ")
                    print(f"Result: {self.operators[operator](a)}")
                except Exception as e:
                    print(f"Error: {str(e)}")

            # Show help (no inputs)
            elif operator == 'help':
                print(self.show_help())

            # Double input operations
            else:
                try:
                    a = self.get_number("Enter first number: ")
                    b = self.get_number("Enter second number: ")
                    print(f"Result: {self.operators[operator](a, b)}")
                except Exception as e:
                    print(f"Error: {str(e)}")

            cont = input("Do you want to continue? (yes/no): ").lower()
            if cont != 'yes':
                print("Exiting calculator. Goodbye!")
                break


if __name__ == "__main__":
    calc = ScientificCalculator()
    calc.calculate()

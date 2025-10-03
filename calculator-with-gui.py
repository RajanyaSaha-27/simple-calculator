import tkinter as tk
from math import sqrt, sin, cos, tan, exp, log, pow, radians, asin, acos, atan, degrees
import ast
from tkinter import simpledialog

class SafeEval:
    """A small safe evaluator for arithmetic expressions."""
    allowed_nodes = {
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num,
        ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow,
        ast.Mod, ast.USub, ast.UAdd, ast.Load, ast.Constant
    }

    @staticmethod
    def eval_expr(expr: str):
        try:
            node = ast.parse(expr, mode='eval')
            if not all(isinstance(n, tuple(SafeEval.allowed_nodes)) for n in ast.walk(node)):
                raise ValueError("Unsafe expression")
            return eval(compile(node, "<string>", "eval"))
        except Exception:
            raise ValueError("Invalid Expression")


class ScientificCalculatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Scientific Calculator")
        self.window.geometry("400x600")

        # Entry field
        self.entry_field = tk.Entry(self.window, width=35, borderwidth=5, font=("Arial", 14))
        self.entry_field.grid(row=0, column=0, columnspan=4, pady=10)

        self.create_top_buttons()
        self.create_number_buttons()
        self.create_basic_operation_buttons()
        self.create_scientific_operation_buttons()

    def create_top_buttons(self):
        tk.Button(self.window, text='C', padx=80, pady=20,
                  command=self.clear_entry).grid(row=1, column=0, columnspan=2, sticky='ew')
        tk.Button(self.window, text='CE', padx=80, pady=20,
                  command=self.backspace_entry).grid(row=1, column=2, columnspan=2, sticky='ew')

    def backspace_entry(self):
        current_text = self.entry_field.get()
        self.entry_field.delete(0, tk.END)
        self.entry_field.insert(0, current_text[:-1])

    def create_number_buttons(self):
        button_texts = ['7', '8', '9',
                        '4', '5', '6',
                        '1', '2', '3',
                        None, '0']

        row_val, col_val = 2, 0
        for text in button_texts:
            if text:
                tk.Button(self.window, text=text, padx=30, pady=20,
                          command=lambda t=text: self.append_to_entry(t)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

    def create_basic_operation_buttons(self):
        operations = ['+', '-', '*', '/']
        row_val = 2
        col_val = 3
        for op in operations:
            tk.Button(self.window, text=op, padx=30, pady=20,
                      command=lambda o=op: self.append_to_entry(o)).grid(row=row_val, column=col_val)
            row_val += 1
        tk.Button(self.window, text='=', padx=30, pady=20,
                  command=self.calculate_result).grid(row=6, column=3)

    def create_scientific_operation_buttons(self):
        scientific_ops = ['sqrt', 'sin', 'cos', 'tan',
                          'exp', 'log', 'pow', 'asin',
                          'acos', 'atan']
        for i in range(3):
            tk.Button(self.window, text=scientific_ops[i], padx=25, pady=15,
                      command=lambda o=scientific_ops[i]: self.scientific_operation(o)).grid(row=6, column=i)
        row_val, col_val = 7, 0
        for i in range(3, len(scientific_ops)):
            tk.Button(self.window, text=scientific_ops[i], padx=25, pady=15,
                      command=lambda o=scientific_ops[i]: self.scientific_operation(o)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def append_to_entry(self, value):
        self.entry_field.insert(tk.END, str(value))

    def clear_entry(self):
        self.entry_field.delete(0, tk.END)

    def calculate_result(self):
        try:
            expr = self.entry_field.get()
            result = SafeEval.eval_expr(expr)
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, str(result))
        except Exception:
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, "Invalid Input")

    def scientific_operation(self, op):
        try:
            num = float(self.entry_field.get())
            self.entry_field.delete(0, tk.END)

            if op == 'sqrt':
                result = sqrt(num)
            elif op == 'sin':
                result = sin(radians(num))
            elif op == 'cos':
                result = cos(radians(num))
            elif op == 'tan':
                result = tan(radians(num))
            elif op == 'exp':
                result = exp(num)
            elif op == 'log':
                result = log(num)
            elif op == 'pow':
                exponent = simpledialog.askfloat("Input", "Enter exponent:", parent=self.window)
                result = pow(num, exponent) if exponent is not None else "Error"
            elif op == 'asin':
                result = degrees(asin(num))
            elif op == 'acos':
                result = degrees(acos(num))
            elif op == 'atan':
                result = degrees(atan(num))
            else:
                result = "Error"

            self.entry_field.insert(tk.END, str(result))
        except Exception:
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, "Invalid Input")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calculator = ScientificCalculatorGUI()
    calculator.run()

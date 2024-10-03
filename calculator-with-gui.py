import tkinter as tk
from math import sqrt, sin, cos, tan, exp, log, pow, radians, asin, acos, atan

class ScientificCalculatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Scientific Calculator")
        self.window.geometry("400x600")

        # Create entry field
        self.entry_field = tk.Entry(self.window, width=35, borderwidth=5)
        self.entry_field.grid(row=0, column=0, columnspan=4)

        # Number buttons
        self.create_number_buttons()

        # Basic arithmetic operation buttons
        self.create_basic_operation_buttons()

        # Scientific operation buttons
        self.create_scientific_operation_buttons()

    def create_number_buttons(self):
        button_texts = ['7', '8', '9',
                        '4', '5', '6',
                        '1', '2', '3',
                        '0']
        
        row_val = 1
        col_val = 0
        
        for text in button_texts:
            tk.Button(self.window, text=text, padx=40, pady=20,
                      command=lambda t=text: self.append_to_entry(t)).grid(row=row_val, column=col_val)
            
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

    def create_basic_operation_buttons(self):
        operations = ['+', '-', '*', '/']
        row_val = 1
        col_val = 3
        
        for op in operations:
            tk.Button(self.window, text=op, padx=39, pady=20,
                      command=lambda o=op: self.append_to_entry(o)).grid(row=row_val, column=col_val)
            row_val += 1

        tk.Button(self.window, text='=', padx=91, pady=20,
                  command=self.calculate_result).grid(row=row_val, column=0, columnspan=4)

    def create_scientific_operation_buttons(self):
        scientific_ops = ['sqrt', 'sin', 'cos', 'tan',
                          'exp', 'log', 'pow', 'asin',
                          'acos', 'atan']

        row_val = 5
        col_val = 0
        
        for i, op in enumerate(scientific_ops):
            tk.Button(self.window, text=op, padx=25, pady=15,
                      command=lambda o=op: self.scientific_operation(o)).grid(row=row_val, column=col_val)
            
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def append_to_entry(self, value):
        current_value = self.entry_field.get()
        self.entry_field.delete(0, tk.END)
        self.entry_field.insert(tk.END, str(current_value) + str(value))

    def calculate_result(self):
        try:
            result = eval(self.entry_field.get())
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, str(result))
        except Exception as e:
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, "Error")

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
                exponent = float(input("Enter exponent: "))
                result = pow(num, exponent)
            elif op == 'asin':
                result = degrees(asin(num))
            elif op == 'acos':
                result = degrees(acos(num))
            elif op == 'atan':
                result = degrees(atan(num))
            
            self.entry_field.insert(tk.END, str(result))
        except Exception as e:
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, "Error")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = ScientificCalculatorGUI()
    calculator.run()

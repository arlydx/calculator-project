import tkinter as tk
from tkinter import messagebox

class CalculatorView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Arly Calculator")
        self.root.geometry("350x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#ff8c00")
        
        self.display_var = tk.StringVar(value="0")
        self.current_value = ""
        self.operation = None
        self.first_operand = None
        
        self.create_widgets()
    
    def create_widgets(self):
        # Ecran
        display = tk.Entry(self.root, textvariable=self.display_var, font=("Arial", 20), 
                          justify="right", bd=5, state="readonly", bg="#fff5e6", fg="#ff6600")
        display.pack(fill=tk.BOTH, pady=10, padx=10)
        
        # Boutons
        buttons_frame = tk.Frame(self.root, bg="#ff8c00")
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        buttons = [
            ['C', '√', '|x|', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '±', '=']
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                # Couleur spéciale pour les opérations
                if text in ['÷', '×', '-', '+', '=']:
                    bg_color = "#ff6600"
                    fg_color = "white"
                elif text in ['C', '√', '|x|', '±']:
                    bg_color = "#ffa500"
                    fg_color = "white"
                else:
                    bg_color = "#ffe4b3"
                    fg_color = "#ff6600"
                
                btn = tk.Button(buttons_frame, text=text, font=("Arial", 16),
                               bg=bg_color, fg=fg_color,
                               command=lambda t=text: self.on_button_click(t))
                btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
        
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)
    
    def on_button_click(self, text):
        if text.isdigit() or text == '.':
            self.append_digit(text)
        elif text in ['+', '-', '×', '÷']:
            self.set_operation(text)
        elif text == '=':
            self.calculate()
        elif text == 'C':
            self.clear()
        elif text == '√':
            self.square_root()
        elif text == '|x|':
            self.absolute_value()
        elif text == '±':
            self.toggle_sign()
    
    def append_digit(self, digit):
        if self.current_value == "0" and digit != '.':
            self.current_value = digit
        elif digit == '.' and '.' in self.current_value:
            return
        else:
            self.current_value += digit
        self.display_var.set(self.current_value)
    
    def set_operation(self, op):
        if self.current_value:
            if self.first_operand is not None and self.operation is not None:
                self.calculate()
            self.first_operand = float(self.current_value)
            self.operation = op
            self.current_value = ""
    
    def calculate(self):
        if self.operation and self.first_operand is not None and self.current_value:
            second_operand = float(self.current_value)
            self.controller.calculate(self.operation, self.first_operand, second_operand)
            self.operation = None
            self.first_operand = None
    
    def clear(self):
        self.current_value = ""
        self.operation = None
        self.first_operand = None
        self.display_var.set("0")
    
    def square_root(self):
        if self.current_value:
            self.controller.square_root(float(self.current_value))
    
    def absolute_value(self):
        if self.current_value:
            self.controller.absolute_value(float(self.current_value))
    
    def toggle_sign(self):
        if self.current_value and self.current_value != "0":
            if self.current_value.startswith('-'):
                self.current_value = self.current_value[1:]
            else:
                self.current_value = '-' + self.current_value
            self.display_var.set(self.current_value)
    
    def show_result(self, result):
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        self.current_value = str(result)
        self.display_var.set(self.current_value)
    
    def show_error(self, message):
        messagebox.showerror("Erreur", message)
        self.clear()

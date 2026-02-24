class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def calculate(self, operation, a, b):
        """Effectue les calculs avec deux opérandes"""
        try:
            if operation == "+":
                result = self.model.add(a, b)
            elif operation == "-":
                result = self.model.subtract(a, b)
            elif operation == "×":
                result = self.model.multiply(a, b)
            elif operation == "÷":
                result = self.model.divide(a, b)
            else:
                raise ValueError("Unknown operation")

            self.view.show_result(result)

        except Exception as err:
            self.view.show_error(str(err))
    
    def square_root(self, a):
        """Calcule la racine carrée"""
        try:
            result = self.model.square_root(a)
            self.view.show_result(result)
        except Exception as err:
            self.view.show_error(str(err))
    
    def absolute_value(self, a):
        """Calcule la valeur absolue"""
        try:
            result = self.model.absolute_value(a)
            self.view.show_result(result)
        except Exception as err:
            self.view.show_error(str(err))
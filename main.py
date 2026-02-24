import tkinter as tk
from model import CalculatorModel
from view import CalculatorView
from controller import CalculatorController

def main():
    # Creer la fenetre principale
    root  = tk.Tk()

    # creer le modele 
    model = CalculatorModel()

    # creer le controleur
    controller = CalculatorController(model, None)

    # creer la vue avec le controleur
    view = CalculatorView(root, controller)

    # Associer la vue au controleur
    controller .view = view

    # Lancer l'application
    root.mainloop()

if __name__ == "__main__":
 main()
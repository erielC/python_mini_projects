import math
import tkinter as tk
from calculator import Calculator

# Prompt the user what operation will be completed starting off with the four basic functions first
operation = int(input("What operation with you be using today?\n[1] Add \n[2] Subtract \n[3] Multiply \n[4] Divide \n"))
calc = Calculator(a, b)

if operation == 1:
    calc.add()
elif operation == 2:
    calc.subtract()
elif operation == 3:
    calc.multiply()
elif operation == 4:
    calc.divide()
else: 
    print("Not an option choose again")
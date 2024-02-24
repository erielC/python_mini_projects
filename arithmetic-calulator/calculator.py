import tkinter as tk

class Calculator: 
    def __init__(self):
        """
        Initializes a new instance of the Calculator class.
        """
        self.root = tk.Tk()
        self.geometry = self.root.geometry("800x600")
        self.root.title("Arithmetic Calculator")
        
        buttomframe = tk.Frame(self.root)
        buttomframe.columnconfigure(0, weight=1)
        buttomframe.columnconfigure(1, weight=1)
        buttomframe.columnconfigure(2, weight=1)
            
        self.btn1 = tk.Button(buttomframe, text="1", font=("Arial", 24))
        self.root.mainloop()
            
Calculator()
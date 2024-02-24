import tkinter as tk

class MyGUI:
    def __init__(self):
        self.window = tk.Tk()
        
        self.title = self.window.title("Arithmetic Calculator")
        
        self.label = tk.Label(self.window, text="Arithmetic Calculator", font=("Arial", 24))
        self.label.pack(padx=10, pady=10)
        
    
        self.textbox = tk.Text(self.window, height=2, width=70, font=("Arial", 24))
        self.textbox.pack(padx=10, pady=10)
        # Linking a keybind to trigger an event
        self.textbox.bind("<Key>", self.add_button)
    
        
        # WHen you press x button it will call an event
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        
        self.button = tk.Button(self.window, text="Calculate", font=("Arial", 24))
        self.button.pack(padx=10, pady=10)
        
        
        self.window.mainloop()

    def add_button(self):
        button = tk.Button(self.window, text="+", font=("Arial", 24))
        button.pack(padx=10, pady=10)
        
    def close(self):
        print("Closing the window...")
        self.window.destroy()
        
MyGUI()
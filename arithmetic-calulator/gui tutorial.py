import tkinter as tk

# Creating a window
window = tk.Tk()

# Setting geometry
window.geometry("800x600")
window.title("Arithmetic Calculator")

label = tk.Label(window, text="Arithmetic Calculator", font=("Arial", 24))
# layout to display on the screen
label.pack(padx=20, pady=20)

textbox = tk.Text(window, height=2, width=70, font=("Arial", 24))
textbox.pack(padx=10)

# Entry is textbox with height 1 ex. username, password
# myentry = tk.Entry(window, font=("Arial", 24))
# myentry.pack()

# Adding a button 
# button = tk.Button(window, text="Calculate", font=("Arial", 24))
# button.pack()

# ////////////////// GRID LAYOUT //////////////////
buttonframe = tk.Frame(window)
buttonframe.columnconfigure(0, weight=1) 
buttonframe.columnconfigure(1, weight=1) 
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=("Arial", 24)) # Buttonframe is the parent as it is in the window
btn1.grid(row=0, column=0, sticky="news") # sticky is used to stretch the button to fill the entire cell

btn2 = tk.Button(buttonframe, text="2", font=("Arial", 24))
btn2.grid(row=0, column=1, sticky="news")

btn3 = tk.Button(buttonframe, text="3", font=("Arial", 24))
btn3.grid(row=0, column=2, sticky="news")

btn4 = tk.Button(buttonframe, text="4", font=("Arial", 24))
btn4.grid(row=1, column=0, sticky="news")

btn5 = tk.Button(buttonframe, text="5", font=("Arial", 24))
btn5.grid(row=1, column=1, sticky="news")

btn6 = tk.Button(buttonframe, text="6", font=("Arial", 24))
btn6.grid(row=1, column=2, sticky="news")

buttonframe.pack(fill="x") #fill the entire width of the window
# packing the frames to display it


window.mainloop()
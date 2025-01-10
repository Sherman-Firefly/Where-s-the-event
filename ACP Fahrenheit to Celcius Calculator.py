from tkinter import *
import math
window=Tk()

window.title("F to C temperature")
window.geometry('400x400')

def submit_form():
    input_value = f1_entry.get()
    
    textbox.delete(1.0, END)
    
    try:
        f1 = float(input_value)
        
        conversion = (f1-32)*5/9
        
        textbox.insert(END, f"{conversion:.3f} C")
    except ValueError:
        textbox.insert(END, "Error: Please enter a valid number.")

Label(window, text="Temperature Conversion Calculator", font=("Arial", 16)).pack(pady=10)

Label(window, text="Fahrenheit:").pack(anchor=W, padx=10)
f1_entry = Entry(window, width=30)
f1_entry.pack(padx=10)

textbox=Text(height=6)

submit_btn = Button(window, text="Submit", command=submit_form)
submit_btn.pack(pady=10)
textbox.pack()
window.mainloop()
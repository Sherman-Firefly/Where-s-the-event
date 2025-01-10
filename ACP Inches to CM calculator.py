from tkinter import *
import math
window=Tk()

window.title("Inches to CM")
window.geometry('300x300')

def submit_form():
    input_value = n1_entry.get()
    
    textbox.delete(1.0, END)
    
    try:
        n1 = float(input_value)
        
        conversion = n1 * 2.54
        
        textbox.insert(END, f"{conversion:.3f} cm")
    except ValueError:
        textbox.insert(END, "Error: Please enter a valid number.")

Label(window, text="Conversion Calculator", font=("Arial", 16)).pack(pady=10)

Label(window, text="Inches:").pack(anchor=W, padx=10)
n1_entry = Entry(window, width=30)
n1_entry.pack(padx=10)

textbox=Text(height=6)

submit_btn = Button(window, text="Submit", command=submit_form)
submit_btn.pack(pady=10)
textbox.pack()
window.mainloop()
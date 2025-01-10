from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Virus Detection")
window.geometry("500x500")

def msg():
    messagebox.showwarning("Halt. Virus found on site. Leave immediately")

button=Button(window,text="Scan for Virus", fg="black", bg="yellow", command=msg)
button.place(x=50,y=100)


window.mainloop()
from tkinter import *

window=Tk()
window.title("Event Handling")
window.geometry("500x500")

def eventHandling(event):
    """Print the chatacter associated to the key pressed"""
    print(event.char)

window.bind("<KeyPress>", eventHandling)

def handler_click(event):
    print("\nThe button was clicked")

button=Button(text="Click Here")
button.pack()

button.bind("<Button-1>",handler_click)

window.mainloop()


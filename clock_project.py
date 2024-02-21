from tkinter import*
from tkinter.ttk import

from time import strftime


root = Tk()
root.title("clock")

def time():
    from time import  gmtime, strftime
    strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background= "black", foreground= "cyan")
label.pack(anchor= 'center')
time()

mainloop()
